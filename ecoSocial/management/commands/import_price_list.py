import os
import re
from django.core.management.base import BaseCommand
from django.conf import settings
from ecoSocial.models import Stock

class Command(BaseCommand):
    help = 'Import stock items from price_list.txt into the Stock model.'

    def handle(self, *args, **options):
        # Use BASE_DIR to construct the path to price_list.txt
        price_list_path = os.path.join(settings.BASE_DIR, 'price_list.txt')
        if not os.path.exists(price_list_path):
            self.stderr.write(self.style.ERROR(f'File not found: {price_list_path}'))
            return

        # Regex for product lines
        product_pattern = re.compile(r'^(?P<size>[\dxX ]+)\s+(?P<name>.+?)\s+EA\s+R(?P<price>[\d ]+)$', re.IGNORECASE)
        current_wood_type = None
        created = 0
        skipped = 0
        total_lines = 0
        matched_lines = 0

        with open(price_list_path, 'r', encoding='utf-8') as f:
            for line in f:
                total_lines += 1
                line = line.strip()
                if not line or line.startswith('~') or line.startswith('MAIN BRANCH') or line.startswith('BUSINESS HOURS'):
                    continue
                m = product_pattern.match(line)
                if m:
                    matched_lines += 1
                    size = m.group('size').replace('X', 'x').replace(' x ', 'x').replace('  ', ' ').strip()
                    name = m.group('name').title().strip()
                    price = float(m.group('price').replace(' ', '').replace(',', ''))
                    wood_type = current_wood_type or 'other'
                    if 'pallet' in name.lower():
                        wood_type = 'pallet'
                    elif 'box' in name.lower():
                        wood_type = 'offcut'
                    elif 'timber' in name.lower() or 'baltic' in name.lower():
                        wood_type = 'plank'
                    stock, created_obj = Stock.objects.get_or_create(
                        name=name,
                        wood_type=wood_type,
                        size=size,
                        defaults={
                            'quantity': 10,
                            'price': price,
                            'description': '',
                        }
                    )
                    if created_obj:
                        created += 1
                        self.stdout.write(f"CREATED: {name} | {wood_type} | {size} | {price}")
                    else:
                        skipped += 1
                else:
                    # Treat as section header if not a product line
                    if line.isupper() or (line and not line[0].isdigit()):
                        current_wood_type = line.lower().replace(' ', '_')
        self.stdout.write(self.style.SUCCESS(f'Import complete. Total lines: {total_lines}, Matched: {matched_lines}, Created: {created}, Skipped: {skipped}'))

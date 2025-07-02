from django.contrib import admin
from .models import Profile, Post, Connection, Message, Stock

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Connection)
admin.site.register(Message)
admin.site.register(Stock)

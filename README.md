# ecoSocial - Django Social Network Application

## Quick Start & Troubleshooting (Latest Steps)

1. **Set the Django Secret Key**
   - Before running Django, set the `DJANGO_SECRET_KEY` environment variable:
     ```bash
     export DJANGO_SECRET_KEY='your-strong-secret-key'
     ```
   - Replace `'your-strong-secret-key'` with a secure, random value.

2. **Install Python and Node.js dependencies**
   - Python:
     ```bash
     pip install -r requirements.txt  # or use pipenv if you use Pipfile
     ```
   - Node.js:
     ```bash
     npm install
     ```

3. **Run Django Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the Django Development Server**
   ```bash
   python manage.py runserver
   ```

5. **Start the Webpack Dev Server (for frontend assets)**
   ```bash
   npm start
   ```

6. **Access the app**
   - Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## Troubleshooting Workspace Features

- If the **Save Note** or **Calculate** features do not work:
  1. Ensure your user has a `Profile` with a `workspace_notes` field. Run all migrations and check the admin panel.
  2. Make sure the `Stock` model has entries for each wood type (add via admin if needed).
  3. Check the Django server logs for errors.
  4. For further debugging, review the `workspace` view in `ecoSocial/views.py` and the `workspace.html` template.

---

## Project Overview

ecoSocial is a custom social network application built using Django, designed to provide a comprehensive social networking experience with features like user registration, profile management, posts, and user connections.

## Features

### User Management
- User registration and authentication
- Profile creation and editing
- Profile picture upload
- Social authentication support

### Social Interactions
- Create and view posts
- Connect with other users
- View user connections

## Technology Stack

- **Backend**: Django 5.2.3
- **Frontend**: Bootstrap
- **Database**: SQLite (development)
- **Authentication**: Django built-in auth, social-auth
- **Additional Libraries**: 
  - django-user-accounts
  - social-auth-app-django
  - Pillow for image handling

## Prerequisites

- Python 3.13
- pip
- virtualenv (recommended)

## Installation

1. Clone the repository:
\\\ash
git clone https://github.com/yourusername/ecoSocial.git
cd ecoSocial
\\\

2. Create a virtual environment:
\\\ash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\\\

3. Install dependencies:
\\\ash
pip install -r requirements.txt
\\\

4. Run migrations:
\\\ash
python manage.py makemigrations
python manage.py migrate
\\\

5. Create a superuser:
\\\ash
python manage.py createsuperuser
\\\

6. Run the development server:
\\\ash
python manage.py runserver
\\\

## Configuration

### Settings
- Adjust \settings.py\ for production deployment
- Configure environment variables for sensitive information
- Set up social authentication backends as needed

## Next Development Steps

1. Implement advanced features:
- Post likes and comments
- User search functionality
- Enhanced social media integration
- Real-time messaging

2. Improve security:
- Add more robust form validation
- Implement detailed user permissions
- Set up HTTPS and secure authentication

3. Performance optimization:
- Add caching mechanisms
- Optimize database queries
- Implement pagination for posts and connections

## Home Page Features for Wood Recycling Company

### 1. Stock Dashboard
- Display latest stock available (images, sizes, types, quantities)
- Filter or tab by wood type (e.g., pallets, planks, offcuts)
- Stock alerts for new or low-stock items

### 2. Community & Interaction
- Company announcements/news/events
- User posts/forum for questions, project sharing, and discussion
- Real-time chat for users to interact with the company and each other

### 3. Quick Actions
- Request pickup/delivery button or form
- Contact company form or info
- User profile/account bar for quick access to profile, orders, or messages

### 4. Visuals & Usability
- Hero image or banner related to recycling/sustainability
- Responsive design for mobile and desktop
- Call to action to register, post, or browse stock

### Example Layout (Wireframe)

```
-------------------------------------------------
| Logo | Menu | Profile/Account Bar             |
-------------------------------------------------
| [Hero Image or Banner: "Welcome to WoodCycle"] |
-------------------------------------------------
| [Latest Stock]   [Announcements/News]         |
| [Stock List/Grid][Community Posts/Forum]      |
-------------------------------------------------
| [Chat Widget]   [Quick Actions/Contact]       |
-------------------------------------------------
| Footer: About | Contact | Social Links        |
-------------------------------------------------
```

### Implementation Plan
- Stock section: Django ListView or custom view for latest stock
- Community posts: Use Post model, display recent posts, allow new posts
- Chat widget: Integrate real-time chat (Channels/WebSocket)
- Announcements: Model or static section for company updates
- Quick actions: Forms or buttons linking to relevant views

## Stock Management Features

- Dedicated Stock model for wood items (name, type, size, quantity, price, image, description, date added)
- Admin interface for adding/editing stock
- Dashboard displays latest stock items with images, type, size, quantity, price, and description
- Easily extendable for more wood types or fields

## How to Use

1. Add new stock items via the Django admin panel
2. Latest stock will automatically appear on the dashboard home page
3. Stock display is dynamic and updates as new items are added

## Contributing

1. Fork the repository
2. Create your feature branch (\git checkout -b feature/AmazingFeature\)
3. Commit your changes (\git commit -m 'Add some AmazingFeature'\)
4. Push to the branch (\git push origin feature/AmazingFeature\)
5. Open a Pull Request

## License

Distributed under the MIT License. See \LICENSE\ for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/ecoSocial](https://github.com/yourusername/ecoSocial)

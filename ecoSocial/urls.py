from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


from ecoSocial import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Dashboard/homepage
    path('workspace/', views.workspace, name='workspace'),  # Project planner
    path('posts/', views.posts, name='posts'),  # Community posts
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('create-post/', views.create_post, name='create_post'),
    path('connections/', views.connections, name='connections'),
    path('connect/<str:username>/', views.connect, name='connect'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('account/social/accounts/', TemplateView.as_view(template_name='account/social.html'), name='account_social_accounts'),
    path('account/social/', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

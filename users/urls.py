from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('', views.home, name='home'),  
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
     path('create_post/', views.create_post, name='create_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

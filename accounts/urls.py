from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Root URL - redirect to profile
    path('', views.ProfileView.as_view(), name='index'),
    
    # Authentication URLs
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'),
    
    # Profile Management URLs
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('details/', views.details_view, name='details'),
    path('profile/fitness-goals/', views.fitness_goals_view, name='fitness_goals'),
    path('profile/activity-history/', views.activity_history_view, name='activity_history'),
] 
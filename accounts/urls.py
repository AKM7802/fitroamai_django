from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'),
    
    # Details
    path('user/details/', views.details_view, name='details'), ## details page 
    # Profile Management URLs
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/fitness-goals/', views.fitness_goals_view, name='fitness_goals'),
    path('profile/activity-history/', views.activity_history_view, name='activity_history'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
] 
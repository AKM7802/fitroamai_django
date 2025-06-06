from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile Management URLs
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/fitness-goals/', views.fitness_goals_view, name='fitness_goals'),
    path('profile/activity-history/', views.activity_history_view, name='activity_history'),
] 
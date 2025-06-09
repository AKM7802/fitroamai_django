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
    path('profile/', views.ProfileView.as_view(), name='profile'), ## profile page
    # path('profile/fitness-goals/', views.fitness_goals_view, name='fitness_goals'), # weight loss, muscle gain, etc.
    path('profile/activity-history/', views.activity_history_view, name='activity_history'),  # previous workouts, calories burned, etc.
    path('profile/workout-details/', views.workout_details_view, name='workout_details'), # workout details
    
    # Gym Visits
    path('gyms/check-in/<int:gym_id>/', views.check_in_view, name='check_in'),
    path('gyms/check-out/<int:visit_id>/', views.check_out_view, name='check_out'),
    
] 
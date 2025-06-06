from django.urls import path
from . import views

app_name = 'ai_trainer'

urlpatterns = [
    # AI Trainer Chat
    path('chat/', views.AIChatView.as_view(), name='chat'),
    
    # Workout Plan Management
    path('generate-plan/', views.workout_plan_generator_view, name='generate_plan'),
    path('plans/', views.WorkoutPlanListView.as_view(), name='plan_list'),
    path('plans/<int:plan_id>/', views.WorkoutPlanDetailView.as_view(), name='plan_detail'),
    path('sessions/<int:session_id>/complete/', views.workout_session_complete_view, name='complete_session'),
    
    # Exercise Library
    path('exercises/', views.exercise_library_view, name='exercise_library'),
    
    # Progress Analysis
    path('progress-analysis/', views.ai_progress_analysis_view, name='progress_analysis'),
] 
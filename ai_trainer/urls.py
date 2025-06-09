from django.urls import path
from . import views

app_name = 'ai_trainer'

urlpatterns = [
    # AI Trainer Chat
    path('chat/', views.AIChatView.as_view(), name='chat'), # chat with the AI trainer
    
    # Workout Plan Management
    # path('generate-plan/', views.workout_plan_generator_view, name='generate_plan'), # generate a workout plan
    
    # path('plans/', views.WorkoutPlanListView.as_view(), name='plan_list'), # list of workout plans
    # path('plans/<int:plan_id>/', views.WorkoutPlanDetailView.as_view(), name='plan_detail'), # detail of a workout plan
    # path('sessions/<int:session_id>/complete/', views.workout_session_complete_view, name='complete_session'),
    
    # Exercise Library
    # path('exercises/', views.exercise_library_view, name='exercise_library'),  ## move from here
    
    # Progress Analysis
    # path('progress-analysis/', views.ai_progress_analysis_view, name='progress_analysis'),  ## move from here
] 
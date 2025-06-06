from django.db import models
from accounts.models import User

class WorkoutPlan(models.Model):
    """
    AI-generated workout plans for users
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Plan parameters
    duration_weeks = models.IntegerField(default=4)
    sessions_per_week = models.IntegerField(default=3)
    fitness_level = models.CharField(max_length=20)
    focus_area = models.CharField(max_length=50)
    
    # Metadata
    ai_version = models.CharField(max_length=50, help_text="Version of AI that generated this plan")
    user_feedback_score = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s {self.title} Plan"
    
    class Meta:
        ordering = ['-created_at']

class WorkoutSession(models.Model):
    """
    Individual workout sessions within a plan
    """
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=100)
    description = models.TextField()
    day_number = models.IntegerField()
    week_number = models.IntegerField()
    duration_minutes = models.IntegerField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Week {self.week_number}, Day {self.day_number}: {self.title}"
    
    class Meta:
        ordering = ['week_number', 'day_number']

class Exercise(models.Model):
    """
    Exercise database for AI to reference
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50)
    difficulty_level = models.CharField(max_length=20, 
                                       choices=[('beginner', 'Beginner'), 
                                                ('intermediate', 'Intermediate'),
                                                ('advanced', 'Advanced')])
    equipment_needed = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    instructions = models.TextField()
    
    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    """
    Link between exercises and workout sessions
    """
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.CharField(max_length=50)  # Could be "12" or "8-12" or "Until failure"
    rest_seconds = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    order = models.IntegerField()
    
    def __str__(self):
        return f"{self.exercise.name} - {self.sets}x{self.reps}"
    
    class Meta:
        ordering = ['order']

class AIChatMessage(models.Model):
    """
    Store conversation history between user and AI trainer
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ai_messages')
    message_text = models.TextField()
    is_user_message = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Context for AI responses
    related_workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.SET_NULL, 
                                            null=True, blank=True)
    
    def __str__(self):
        sender = "User" if self.is_user_message else "AI"
        return f"{sender}: {self.message_text[:50]}..."
    
    class Meta:
        ordering = ['timestamp'] 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    """
    Extended User model to add additional fields for fitness app users
    """
    # Personal Info
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    # Fitness Profile
    height = models.FloatField(blank=True, null=True, help_text="Height in cm")
    weight = models.FloatField(blank=True, null=True, help_text="Weight in kg")
    fitness_level = models.CharField(max_length=20, blank=True, null=True, 
                                     choices=[('beginner', 'Beginner'), 
                                              ('intermediate', 'Intermediate'),
                                              ('advanced', 'Advanced')])
    fitness_goals = models.TextField(blank=True, null=True)
    
    # Preferences
    preferred_workout_type = models.CharField(max_length=50, blank=True, null=True)
    workout_frequency = models.IntegerField(blank=True, null=True, help_text="Days per week")
    
    # App settings
    notification_preferences = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return self.username

class UserActivity(models.Model):
    """
    Track user activity and app usage
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)  # login, workout_completed, etc.
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(default=dict, blank=True)
    
    class Meta:
        verbose_name_plural = "User Activities"
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} - {self.timestamp}" 
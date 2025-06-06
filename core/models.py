from django.db import models
from accounts.models import User

class Notification(models.Model):
    """
    System notifications for users
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    # Notification types
    TYPE_CHOICES = [
        ('system', 'System'),
        ('membership', 'Membership'),
        ('workout', 'Workout'),
        ('gym_access', 'Gym Access'),
        ('payment', 'Payment'),
    ]
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='system')
    
    # Associated content object
    content_type = models.CharField(max_length=50, blank=True, null=True)
    content_id = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
    class Meta:
        ordering = ['-timestamp']

class Feedback(models.Model):
    """
    User feedback for the app
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    subject = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Status tracking
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    admin_notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.subject}"
    
    class Meta:
        ordering = ['-timestamp']

class AppSetting(models.Model):
    """
    Global application settings
    """
    key = models.CharField(max_length=50, unique=True)
    value = models.JSONField()
    description = models.TextField(blank=True, null=True)
    
    # Setting groups for organization
    GROUP_CHOICES = [
        ('general', 'General'),
        ('membership', 'Membership'),
        ('ai', 'AI'),
        ('payment', 'Payment'),
        ('gym', 'Gym'),
        ('security', 'Security'),
    ]
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, default='general')
    
    # Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.key} ({self.group})" 
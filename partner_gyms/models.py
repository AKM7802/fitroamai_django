from django.db import models
from accounts.models import User
from membership.models import UserMembership

class PartnerGym(models.Model):
    """
    Partner gym that allows access to FitRoamAI users
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    # Contact Information
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    
    # Business Details
    business_hours = models.JSONField(default=dict)  # Store hours for each day
    amenities = models.JSONField(default=list)  # List of amenities
    
    # Access Control
    requires_reservation = models.BooleanField(default=False)
    max_daily_visitors = models.IntegerField(null=True, blank=True)
    access_instructions = models.TextField(blank=True, null=True)
    
    # Status
    is_active = models.BooleanField(default=True)
    
    # Admin and Management
    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, 
                                   related_name='managed_gyms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"
    
    class Meta:
        ordering = ['name']

class GymMembership(models.Model):
    """
    Connect users to their selected partner gyms
    """
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE, 
                                        related_name='gym_memberships')
    partner_gym = models.ForeignKey(PartnerGym, on_delete=models.CASCADE, 
                                   related_name='user_memberships')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    # Access code/QR for gym entry
    access_code = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.user_membership.user.username} at {self.partner_gym.name}"
    
    class Meta:
        unique_together = ['user_membership', 'partner_gym']

class GymVisit(models.Model):
    """
    Track user visits to partner gyms
    """
    gym_membership = models.ForeignKey(GymMembership, on_delete=models.CASCADE, related_name='visits')
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    
    # Additional Data
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.gym_membership.user_membership.user.username} visited {self.gym_membership.partner_gym.name} on {self.check_in_time.date()}"

class GymReview(models.Model):
    """
    Store user reviews and ratings for partner gyms
    """
    gym_membership = models.ForeignKey(GymMembership, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.gym_membership.user_membership.user.username} rated {self.gym_membership.partner_gym.name} {self.rating}/5"
    
    class Meta:
        unique_together = ['gym_membership']  # One review per gym membership 
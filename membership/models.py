from django.db import models
from accounts.models import User

class MembershipPlan(models.Model):
    """
    Available membership plans for users
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_monthly = models.DecimalField(max_digits=8, decimal_places=2)
    price_yearly = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    
    # Features
    includes_ai_trainer = models.BooleanField(default=True)
    includes_partner_gym_access = models.BooleanField(default=False)
    max_partner_gyms = models.IntegerField(default=0)
    custom_workout_plans_per_month = models.IntegerField(default=1)
    
    # Other Plan Details
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class UserMembership(models.Model):
    """
    Track user memberships and subscription status
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='membership')
    membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.PROTECT)
    
    # Subscription Status
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('expired', 'Expired'),
        ('trial', 'Trial'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='trial')
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Payment Tracking
    last_payment_date = models.DateField(null=True, blank=True)
    next_payment_date = models.DateField(null=True, blank=True)
    
    # Subscription details
    is_annual = models.BooleanField(default=False)
    auto_renew = models.BooleanField(default=True)
    
    # External payment details
    payment_provider = models.CharField(max_length=50, null=True, blank=True)  # e.g., 'stripe', 'paypal'
    payment_provider_subscription_id = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.membership_plan.name}"
    
    @property
    def is_active(self):
        return self.status == 'active' or self.status == 'trial'

class Payment(models.Model):
    """
    Track payment history
    """
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    # Payment details
    payment_method = models.CharField(max_length=50)  # e.g., 'credit_card', 'paypal'
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='completed')
    
    # Additional info
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user_membership.user.username} - {self.amount} - {self.payment_date.date()}"

class BillingInfo(models.Model):
    """
    Store user billing information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='billing_info')
    
    # Billing address
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    # Billing contact
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    
    # Masked payment info (for display only)
    # Real payment details should be stored with payment processor
    last_four_digits = models.CharField(max_length=4, blank=True, null=True)
    card_type = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Billing Info" 
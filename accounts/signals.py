from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserActivity
from membership.models import UserMembership, MembershipPlan

@receiver(post_save, sender=User)
def create_user_membership(sender, instance, created, **kwargs):
    """
    When a new user is created, automatically create a trial membership for them
    """
    if created:
        # Log the user creation
        UserActivity.objects.create(
            user=instance,
            activity_type='user_created',
            details={'source': 'registration'}
        )
        
        # This will be implemented once membership app is fully set up
        # Try to get a trial plan
        # trial_plan = MembershipPlan.objects.filter(name__icontains='trial').first()
        # if trial_plan:
        #     UserMembership.objects.create(
        #         user=instance,
        #         membership_plan=trial_plan,
        #         status='trial',
        #         start_date=datetime.date.today(),
        #         end_date=datetime.date.today() + datetime.timedelta(days=30),
        #     ) 
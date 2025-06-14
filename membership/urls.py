from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    # Membership Plans
    path('plans/', views.membership_plans_view, name='plans'), ## list of membership plans
    path('my-membership/', views.UserMembershipView.as_view(), name='my_membership'),
    path('cancel/', views.cancel_subscription_view, name='cancel'),
    path('upgrade/', views.upgrade_membership_view, name='upgrade'),
    
    # Billing
    path('payment-history/', views.payment_history_view, name='payment_history'), 
    
    # Subscription
    path('subscribe/<int:plan_id>/', views.subscribe_view, name='subscribe'), 
    path('process-payment/', views.process_payment_view, name='process_payment'), 
    path('webhook/payment/', views.payment_webhook_view, name='payment_webhook'),
] 
from django.contrib import admin
from .models import MembershipPlan, UserMembership, Payment, BillingInfo

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_monthly', 'price_yearly', 'includes_ai_trainer', 
                   'includes_partner_gym_access', 'max_partner_gyms', 'is_active')
    list_filter = ('is_active', 'includes_ai_trainer', 'includes_partner_gym_access')
    search_fields = ('name', 'description')

class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_plan', 'status', 'start_date', 'end_date', 'is_annual', 'auto_renew')
    list_filter = ('status', 'membership_plan', 'is_annual', 'auto_renew')
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'start_date'
    inlines = [PaymentInline]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user_membership', 'amount', 'payment_date', 'payment_method', 'status')
    list_filter = ('payment_method', 'status', 'payment_date')
    search_fields = ('user_membership__user__username', 'transaction_id')
    date_hierarchy = 'payment_date'

class BillingInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state', 'country', 'card_type')
    list_filter = ('country', 'state', 'card_type')
    search_fields = ('user__username', 'user__email', 'address_line1', 'city')

# Register models
admin.site.register(MembershipPlan, MembershipPlanAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(BillingInfo, BillingInfoAdmin) 
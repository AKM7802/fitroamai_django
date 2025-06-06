from django.contrib import admin
from .models import PartnerGym, GymMembership, GymVisit, GymReview

class GymMembershipInline(admin.TabularInline):
    model = GymMembership
    extra = 0

class GymVisitInline(admin.TabularInline):
    model = GymVisit
    extra = 0
    fk_name = 'gym_membership'

class GymReviewInline(admin.TabularInline):
    model = GymReview
    extra = 0

class PartnerGymAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country', 'is_active', 'requires_reservation')
    list_filter = ('is_active', 'requires_reservation', 'country', 'state')
    search_fields = ('name', 'description', 'address_line1', 'city')
    inlines = [GymMembershipInline]

class GymMembershipAdmin(admin.ModelAdmin):
    list_display = ('user_display', 'partner_gym', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'partner_gym')
    search_fields = ('user_membership__user__username', 'partner_gym__name')
    date_hierarchy = 'start_date'
    inlines = [GymVisitInline, GymReviewInline]
    
    def user_display(self, obj):
        return obj.user_membership.user.username
    user_display.short_description = 'User'

class GymVisitAdmin(admin.ModelAdmin):
    list_display = ('gym_membership', 'check_in_time', 'check_out_time')
    list_filter = ('check_in_time',)
    search_fields = ('gym_membership__user_membership__user__username', 'gym_membership__partner_gym__name')
    date_hierarchy = 'check_in_time'

class GymReviewAdmin(admin.ModelAdmin):
    list_display = ('gym_membership', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('gym_membership__user_membership__user__username', 'gym_membership__partner_gym__name', 'review_text')
    date_hierarchy = 'created_at'

# Register models
admin.site.register(PartnerGym, PartnerGymAdmin)
admin.site.register(GymMembership, GymMembershipAdmin)
admin.site.register(GymVisit, GymVisitAdmin)
admin.site.register(GymReview, GymReviewAdmin) 
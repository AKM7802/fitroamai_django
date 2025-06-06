from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserActivity

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'fitness_level')
    fieldsets = UserAdmin.fieldsets + (
        ('Fitness Profile', {'fields': ('phone_number', 'date_of_birth', 'height', 'weight', 
                                       'fitness_level', 'fitness_goals', 'preferred_workout_type', 
                                       'workout_frequency', 'notification_preferences')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Fitness Profile', {'fields': ('phone_number', 'date_of_birth', 'height', 'weight', 
                                       'fitness_level', 'fitness_goals', 'preferred_workout_type', 
                                       'workout_frequency')}),
    )
    list_filter = UserAdmin.list_filter + ('fitness_level',)
    search_fields = UserAdmin.search_fields + ('phone_number',)

class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'timestamp')
    list_filter = ('activity_type', 'timestamp')
    search_fields = ('user__username', 'activity_type')
    date_hierarchy = 'timestamp'

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserActivity, UserActivityAdmin) 
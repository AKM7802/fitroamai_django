from django.contrib import admin
from .models import Notification, Feedback, AppSetting

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'notification_type', 'timestamp', 'is_read')
    list_filter = ('notification_type', 'is_read', 'timestamp')
    search_fields = ('user__username', 'title', 'message')
    date_hierarchy = 'timestamp'

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'rating', 'status', 'timestamp')
    list_filter = ('rating', 'status', 'timestamp')
    search_fields = ('user__username', 'subject', 'message')
    date_hierarchy = 'timestamp'

class AppSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'group', 'description_short', 'updated_at')
    list_filter = ('group', 'updated_at')
    search_fields = ('key', 'description')
    
    def description_short(self, obj):
        return obj.description[:50] + '...' if obj.description and len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'

# Register models
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(AppSetting, AppSettingAdmin) 
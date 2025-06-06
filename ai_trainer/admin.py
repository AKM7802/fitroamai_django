from django.contrib import admin
from .models import WorkoutPlan, WorkoutSession, Exercise, WorkoutExercise, AIChatMessage

class WorkoutSessionInline(admin.TabularInline):
    model = WorkoutSession
    extra = 0

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 0

class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'fitness_level', 'focus_area', 'created_at')
    list_filter = ('fitness_level', 'created_at')
    search_fields = ('title', 'user__username', 'description')
    date_hierarchy = 'created_at'
    inlines = [WorkoutSessionInline]

class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'workout_plan', 'day_number', 'week_number', 'completed')
    list_filter = ('completed', 'week_number')
    search_fields = ('title', 'workout_plan__title')
    inlines = [WorkoutExerciseInline]

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group', 'difficulty_level', 'equipment_needed')
    list_filter = ('muscle_group', 'difficulty_level')
    search_fields = ('name', 'description', 'instructions')

class AIChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_user_message', 'timestamp', 'short_message')
    list_filter = ('is_user_message', 'timestamp')
    search_fields = ('user__username', 'message_text')
    date_hierarchy = 'timestamp'
    
    def short_message(self, obj):
        return obj.message_text[:50] + '...' if len(obj.message_text) > 50 else obj.message_text
    short_message.short_description = 'Message'

# Register models
admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(WorkoutSession, WorkoutSessionAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(AIChatMessage, AIChatMessageAdmin) 
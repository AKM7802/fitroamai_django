from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home and Dashboard
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'), ## all the dashboard details
    
    # Notifications
    # path('notifications/', views.notifications_view, name='notifications'), 
    # path('notifications/<int:notification_id>/mark-read/', views.mark_notification_read_view, name='mark_notification_read'),
    
    # Feedback
    path('feedback/', views.FeedbackView.as_view(), name='feedback'), # implement later
    
    # Search
    # path('search/', views.search_view, name='search'),  ## search for gyms, exercises, etc.
    
    # Admin Tools
    # path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'), ## rename to gym dashboard
    # path('app-settings/', views.app_settings_view, name='app_settings'), ## app settings, notifications, etc.
]

# Register error handlers
handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500' 
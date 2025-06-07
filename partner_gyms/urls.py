from django.urls import path
from . import views

app_name = 'partner_gyms'

urlpatterns = [
    # Public Gym Listing
    path('', views.gym_list_view, name='gym_list'),
    path('<int:gym_id>/', views.gym_detail_view, name='gym_detail'),
    
    # User Gym Access
    path('my-gyms/', views.my_gyms_view, name='my_gyms'),
    path('add-membership/<int:gym_id>/', views.add_gym_membership_view, name='add_membership'),
    path('remove-membership/<int:gym_id>/', views.remove_gym_membership_view, name='remove_membership'),
    
    path('qr-code/<int:gym_id>/', views.gym_qr_code_view, name='qr_code'),
    
    # Gym Visits
    path('check-in/<int:gym_id>/', views.check_in_view, name='check_in'),
    path('check-out/<int:visit_id>/', views.check_out_view, name='check_out'),
    path('visit-history/', views.visit_history_view, name='visit_history'),
    
    # Reviews
    path('review/<int:gym_id>/', views.GymReviewView.as_view(), name='review'),
    
    # Gym Admin
    path('admin-dashboard/', views.gym_admin_dashboard_view, name='admin_dashboard'),
    path('access-logs/<int:gym_id>/', views.gym_access_logs_view, name='access_logs'),
] 
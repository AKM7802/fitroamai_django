from django.urls import path
from . import views

app_name = 'partner_gyms'

urlpatterns = [
    
    
    # # integrate auth provider
    # Authentication
    path('gyms/register/', views.register_view, name='register'), ## register a gym 
    path('gyms/login/', views.login_view, name='login'), 
    
    # Public Gym Listing
    path('gyms/', views.gym_list_view, name='gym_list'), ## list of gyms 
    ## detail of a gym ## patch req to update slots
    path('gyms/<int:gym_id>/', views.gym_detail_view, name='gym_detail'), 
    
    # User Gym Access
    # path('my-gyms/', views.my_gyms_view, name='my_gyms'), ## my gyms
    
    path('gyms/qr-code/<int:gym_id>/', views.gym_qr_code_view, name='qr_code'),
    
    # Reviews
    # path('gyms/review/<int:gym_id>/', views.GymReviewView.as_view(), name='review'),
    
    # Gym Admin
    path('gyms/dashboard/', views.gym_admin_dashboard_view, name='admin_dashboard'),
    # path('gyms/access-logs/<int:gym_id>/', views.gym_access_logs_view, name='access_logs'),
] 
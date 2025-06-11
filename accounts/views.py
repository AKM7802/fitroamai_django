from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import User

# User Registration and Authentication Views
def register_view(request):
    """
    Handle user registration
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'accounts/register.html')

        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('accounts:profile')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return render(request, 'accounts/register.html')

    return render(request, 'accounts/register.html')

def login_view(request):
    """
    Handle user login
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')

@login_required
def details_view(request):
    """
    Display and update detailed user information
    """
    if request.method == 'POST':
        user = request.user
        
        # Update user details
        user.phone_number = request.POST.get('phone_number')
        user.date_of_birth = request.POST.get('date_of_birth') or None
        user.height = request.POST.get('height') or None
        user.weight = request.POST.get('weight') or None
        user.fitness_level = request.POST.get('fitness_level')
        user.fitness_goals = request.POST.get('fitness_goals')
        user.preferred_workout_type = request.POST.get('preferred_workout_type')
        user.workout_frequency = request.POST.get('workout_frequency') or None

        try:
            user.save()
            messages.success(request, 'Profile details updated successfully!')
            return redirect('accounts:profile')
        except Exception as e:
            messages.error(request, f'Failed to update profile: {str(e)}')
    
    return render(request, 'accounts/details.html')

# User Profile Management
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    """
    Display and update user profile
    """
    def get(self, request):
        """
        Display user profile
        """
        return render(request, 'accounts/profile.html', {'user': request.user})
    
    def post(self, request):
        """
        Update user profile
        """
        # Profile update logic will be implemented here
        pass

@login_required
def fitness_goals_view(request):
    """
    Allow users to set and update their fitness goals
    """
    # Fitness goals logic will be implemented here
    pass

@login_required
def activity_history_view(request):
    """
    Display user activity history
    """
    # Activity history logic will be implemented here
    pass 
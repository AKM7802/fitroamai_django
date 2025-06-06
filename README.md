# FitRoamAI - AI-Powered Fitness Platform with Partner Gym Access

FitRoamAI is a comprehensive fitness platform that combines AI-driven personalized workout plans with access to a network of partner gyms, offering users flexibility and expert guidance wherever they go.

## Features

- **AI Personal Trainer**
  - Personalized workout plans based on user goals and fitness level
  - Real-time workout adjustments based on progress
  - Interactive chat interface for fitness guidance
  - Progress tracking and analysis

- **Partner Gym Network**
  - Access to multiple partner gyms with a single membership
  - QR code-based gym access
  - Gym discovery and filtering
  - Visit tracking and gym ratings

- **Membership Management**
  - Tiered membership plans
  - Subscription management
  - Payment processing
  - Billing history

- **User Profile**
  - Comprehensive fitness profile
  - Workout history and achievements
  - Personal goal setting
  - Progress visualization

## Project Structure

The project is organized into several Django apps:

- **accounts**: User authentication, profiles, and activity tracking
- **ai_trainer**: AI-driven workout planning and training functionality
- **membership**: Subscription plans, billing, and payment processing
- **partner_gyms**: Gym partner management, access control, and visit tracking
- **core**: Shared functionality like notifications, feedback, and application settings

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (development), PostgreSQL (production)
- **AI Integration**: Machine Learning models for workout planning
- **Authentication**: Django's built-in authentication system
- **Payment Processing**: Integration with payment gateways (e.g., Stripe)

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.2+
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/FitRoamAI.git
   cd FitRoamAI
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Development Roadmap

- **Phase 1**: User authentication, profiles, and basic UI setup
- **Phase 2**: AI trainer integration and workout plan generation
- **Phase 3**: Membership and subscription management
- **Phase 4**: Partner gym integration and access control
- **Phase 5**: Mobile app development and advanced AI features

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/FitRoamAI](https://github.com/yourusername/FitRoamAI) 
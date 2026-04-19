# Gym_Backend-Django - Gym Training Platform Using Computer Vision

A Django REST Framework-based backend platform that enables users to track their fitness journey and receive AI-powered feedback on exercise form through computer vision analysis.

## 🎯 Overview

The Project is a comprehensive gym training platform where users can:
- Select exercises from a curated library
- Perform exercises in front of a camera
- Track progress through personalized dashboard
- Monitor your workout statistics and improvements over time
- Receive real-time AI feedback on form correctness (coming soon)

## ✨ Features

### Current Features
- **Customized User-Model**
- **User Authentication**: email-based OTP login system with JWT token (in develpment stage, code is accessible in Terminal)
- **User Profiles**: Personalized user accounts with profile management
- **Progress Dashboard**: Track workout history and performance metrics
- **Exercise Library**: Comprehensive database of exercises

### 🚀 Upcoming Features
- **AI Form Validation**: Real-time exercise form analysis using MediaPipe
  - Automatic repetition counting
  - Form correctness feedback
  - Exercise duration tracking
  - Currently implemented as standalone feature, integration in progress

## 🛠️ Tech Stack

- **Framework**: Django + Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **OTP System**: Redis-based token caching
- **AI/CV**: MediaPipe (for exercise detection)
- **Containerization**: Docker & Docker Compose

## 📋 Requirements

- Python 3.x
- Docker & Docker Compose
- Redis


## 🚀 Installation & Setup

### Using Docker (Recommended):

1. **Clone the repository**
```bash
   git clone https://github.com/mohamadArdebili/Gym_Backend-Django.git
   docker-compose up --build -d
   cd Gym_Backend-Django
```
### Manual Setup:
1. **Create virtual environment**
  ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. **Install dependencies**
```
   pip install -r requirements.txt
```
3. **Run migrations & Start development server**
```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
```
## 🔐 Authentication Flow
- User enters email address
- System generates OTP and caches it in Redis
- OTP sent to user’s email
- User submits OTP code
- System validates and issues JWT token
- Token used for subsequent authenticated requests

## 📁 Project Structure
Gym_Backend-Django/
├── apps/                
├── config/               
├── requirements.txt      
├── docker-compose.yml    
├── Dockerfile           
└── manage.py           

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/request-otp/` - Request OTP code
- `POST /api/auth/verify-otp/` - Verify OTP and get JWT token
- `POST /api/auth/refresh/` - Refresh JWT token

### User Profile
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile

### Progress & Dashboard
- `GET /api/progress/` - Get user progress data
- `GET /api/dashboard/` - Get dashboard statistics

## Author
Mohamad Ardebili

GitHub:
https://github.com/mohamadArdebili

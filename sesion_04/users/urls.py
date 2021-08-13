"""Users app URLS"""

from django.urls import path

from . import views


app_name = "users"
urlpatterns = [
    # Function Based Views
    # path("login", views.users_login, name="login"),
    # path("logout", views.users_logout, name="logout"),
    # path("signup", views.sign_up, name="signup"),
    # path("me", views.profile, name="profile"),

    # Class based views
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("me", views.ProfileView.as_view(), name="profile"),
]

from django.urls import path
from . import views
from knox import views as knox_views


urlpatterns = [

    path("register", views.RegisterAPIView.as_view(), name="register"),
    path("update", views.UpdateUserAPIView.as_view(), name="update"),
    path("login", views.LoginAPIView.as_view(), name="login"),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path("test", views.TestingAPIView.as_view(), name="test"),
    path("user_profiles", views.UserProfilesAPIView.as_view(), name="user_profiles")

]

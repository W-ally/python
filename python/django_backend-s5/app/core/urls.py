from django.urls import path
from . import views
from .routes import router

urlpatterns = [
   path('/status', views.StatusView.as_view()),
   path('/register', views.RegisterView.as_view()),
   path('/login', views.LoginView.as_view()),
   path('/user', views.UserView.as_view()),
   path('/logout', views.LogoutView.as_view()),
]

urlpatterns += router.urls
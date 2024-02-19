from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("insight/<int:pk>/", views.detailview, name="detail"),
	path("login/", views.logview, name="login"),
	path("model-form/", views.modelform, name = "model-form"),
	path("logout/",views.lg, name="logout"),
]
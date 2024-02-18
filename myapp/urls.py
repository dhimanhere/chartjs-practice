from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("insight/<int:pk>/", views.detailview, name="detail")
]
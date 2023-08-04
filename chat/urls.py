from django.urls import path
from . import views

urlpatterns = [
    path("", views.role_playing_room_list, name="role_playing_room_list"),  # 🔥 HERE
    path('new/', views.role_playing_room_new, name="role_playing_room_new"),
    path("<int:pk>/edit/", views.role_playing_room_edit, name="role_playing_room_edit"),
]

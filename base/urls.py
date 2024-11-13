from django.urls import path
from base import views

urlpatterns = [
    path("", views.home, name="home"),
    path("base/tasks/", views.tasks, name="tasks"),
    path("base/tasks/deltask/<int:t_id>", views.delete, name="deltasks"),
    path("base/tasks/updtask/<int:u_id>/", views.update, name="updtasks"),  # For displaying the form
    path("base/tasks/doupdtask/<int:u_id>/", views.doupdate, name="doupdtasks"),  # For processing the form
]

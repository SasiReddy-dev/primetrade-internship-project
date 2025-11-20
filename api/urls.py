from django.urls import path
from . import views  # import the whole views module

urlpatterns = [
    # Auth
    path("api/v1/register/", views.register),
    path("api/v1/login/", views.login),

    # Task CRUD
    path("api/v1/tasks/", views.get_tasks),
    path("api/v1/tasks/create/", views.create_task),
    path("api/v1/tasks/<int:id>/update/", views.update_task),

    # Delete task endpoints
    path("api/v1/tasks/<int:id>/delete/", views.delete_task),        # Admin only
    path("api/v1/tasks/<int:id>/delete-own/", views.delete_own_task), # Regular user
]

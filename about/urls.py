from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.TodoListView.as_view(), name="about-home"),
    path("about/<int:pk>/", views.TodoDetailView.as_view(), name="todo-detail"),
    path("about/<int:pk>/update/", views.TodoUpdateView.as_view(), name="todo-update"),
    path("about/<int:pk>/delete/", views.TodoDeleteView.as_view(), name="todo-delete"),
    path("about/new/", views.TodoCreateView.as_view(), name="todo-create"),
]

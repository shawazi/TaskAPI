from django.urls import path
from .views import home, task_view, task_detail, TaskView, TaskDetail, TaskCRUD
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("all", TaskCRUD)

urlpatterns = [
    path('', home),
    path('task/', task_view),
    path("task/<int:id>/", task_detail),
    path("details/",TaskView.as_view()),
    path("details/<int:id>",TaskDetail.as_view()),
] + router.urls
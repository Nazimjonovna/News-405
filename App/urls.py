from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateNewsView.as_view()),
    path('getapi/', GetAllNewsView.as_view()),
    path('getgenerics/', GetALlNewView.as_view()),
    path('getone/<int:id>/', GetOneNewsView.as_view()),
    path('get-unreaded/', GetNotificationUnreadedView.as_view()),
    path('change-status/', ChangeStatusNotificationView.as_view()),
]
from django.urls import path

from .views import HomeView

urlpatterns = [
    path('home/<parameter>', HomeView.as_view()),
    path('home/', HomeView.as_view()),
    path('', HomeView.as_view()),
]
from django.urls import path 
from timeline_api import views as timeline_view 

urlpatterns = [
    path('', timeline_view.CardList.as_view()),
]
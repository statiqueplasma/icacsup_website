from django.urls import path
from .views import HomeView, ArticleView, contact, ProgrammeView

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('article/<str:pk>', ArticleView.as_view() , name='article'),
    path('parcours/<str:pk>', ProgrammeView.as_view() , name='programme'),
    path('contact', contact, name='contact'),
]

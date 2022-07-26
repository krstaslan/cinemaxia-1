from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    # i couldnt use it due to some technical problem in my computer
    # path('', TemplateView.as_view(template_name='index.html'))
    path('movie/<str:pk>', views.movie, name="movie"),
 
]
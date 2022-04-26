from django.urls import path, reverse
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='index'),
    path('current_time', views.current_time, name='time_now'),
    path('work_dir', views.workdir, name='work_directories')

]


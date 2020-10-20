from . import views
from django.urls import path

app_name='hobbies'
urlpatterns = [
    path('',views.index, name="index")
]
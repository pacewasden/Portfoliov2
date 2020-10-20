from . import views
from django.urls import path

app_name='hobbies'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int: hobbie_id>',views.detail, name="detail"),
]
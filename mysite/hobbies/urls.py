from . import views
from django.urls import path

app_name='hobbies'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:hobby_id>', views.detail, name='detail'),
    path('item/', views.item, name="item")
]
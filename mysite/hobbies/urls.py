from . import views
from django.urls import path

app_name='hobbies'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:hobby_id>', views.detail, name='detail'),
    path('item/', views.item, name="item"),
    path('add', views.create_hobby, name="create_hobby"),
    path('update/<int:id>', views.update_hobby, name="update_hobby"),
    path('delete/<int:id>', views.delete_hobby, name='delete_hobby'),
]
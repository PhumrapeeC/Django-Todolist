from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<int:todo_id>/', views.update_todo_status, name='update_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]

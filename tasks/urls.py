from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/',views.tasks, name= "tasks"),    
    path('completed_tasks/',views.completed_tasks, name= "completed_tasks"),  
    path('tasks/create/',views.create_task, name= "create_task"),    
    path('tasks/detail/<int:id>/',views.task_detail, name= "task_detail"), 
    path('tasks/update/<int:id>/',views.update, name= "update"), 
    path('tasks/completed/<int:id>/',views.completed_task, name= "completed_task"), 
] 
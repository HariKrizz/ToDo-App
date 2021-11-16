from . import views
from django.urls import path


urlpatterns = [
    path('',views.first,name='first'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:task_id>',views.update,name='update'),
    path('task/', views.resultView,name='resultView'),

    # ListView -- contextobjectview -- cbvtask and DetailView as cbvdetail
    path('cbvtask/',views.TaskListView.as_view(),name='cbvtask'),
    path('cbvdetail/<int:pk>',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>',views.TaskDeleteView.as_view(),name='cbvdelete')
]

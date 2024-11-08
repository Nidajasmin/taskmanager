from django.urls import path
from .views import DashboardView,AddTaskView,deletetaskview,edittaskview


urlpatterns = [
    
    # path('dash',Dashboardview ,name='dashboard'),
    path('dash',DashboardView.as_view() ,name='dashboard'),
    path('add',AddTaskView.as_view() ,name='add'),
    path('delete/<int:id>',deletetaskview.as_view(),name='delete'),
    path('edit/<int:id>',edittaskview.as_view(),name='edit')


]
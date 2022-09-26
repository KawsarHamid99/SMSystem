from django.urls import path
from . import views
urlpatterns=[ 
    path("",views.Homeclass.as_view(),name="home"),
    
    path("<int:id>",views.view_studentClass.as_view(),name="view_student"),
    #path('add/', views.add, name='add'),
    path('add/',views.addclass.as_view(),name='add'),
    #path('edit/<int:id>/', views.edit, name='edit'),
    path('edit/<int:id>/', views.editClass.as_view(), name='edit'),
    path('delete/<int:id>/', views.DeleteClass.as_view(), name='delete'),
    
]
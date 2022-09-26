from django.urls import path
from . import views

urlpatterns=[ 
    path("<int:id>/",views.ResultClass.as_view(),name='results'),
    path('edit/<int:id>/<int:roll>/', views.EditClass.as_view(), name='resultEdit'),
]
from django.urls import path
from . import views

urlpatterns=[ 
    path("<int:id>/",views.result,name='results'),
    path('edit/<int:id>/<int:roll>/', views.edit, name='resultEdit'),
]
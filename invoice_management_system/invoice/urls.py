

from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.updateinvoice, name = 'update'),
    path('delete/<int:id>/', views.deleteinvoice, name = 'delete')

]
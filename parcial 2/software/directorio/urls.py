from django.urls import include, path
from . import views

app_name = 'directorio'

urlpatterns = [
    path('', views.index, name='index'),
    path('sofwaredepa/<str:name>/', views.index_filter, name='index_filter'),
    path('detalles/<int:id>/', views.details, name='detalles'),
    path('nuevo_soft/', views.nuevo_soft, name='nuevo_soft'),
    path('nuevo_dept/', views.nuevo_dept, name='nuevo_dwpt'),

]

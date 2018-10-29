from django.contrib import admin
from django.urls import path

from trabajos import views

app_name="trabajo"

urlpatterns = [
    path('',views.AllList.as_view(), name="index_view"),
    path('create/',views.Create.as_view(), name="create_document"),
    path('allList/',views.AllList.as_view(), name="list_all" ),
    path('listComp/',views.ListComp.as_view(), name="list_comp" ),
    path('listMed/',views.ListMed.as_view(), name="list_med" ),
    path('listNat/',views.ListNat.as_view(), name="list_nat" ),
    path('listSoc/',views.ListSoc.as_view(), name="list_soc" ),
    path('listTierra/',views.ListTierra.as_view(), name="list_tierra" ),
    path('update/<int:pk>', views.UpdateTrabajo.as_view(), name= "update_trabajo"),
    path('delete/<int:pk>', views.DeleteTrabajo.as_view(), name = "delete_trabajo"),
]

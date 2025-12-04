from django.contrib import admin
from django.urls import path
from tripadvisor.views.atracao import AtracaoDetailsView, AtracaoListView, AtracaoDeleteView, AtracaoCreateView, \
AtracaoUpdateView


app_name = 'tripadvisor'

urlpatterns = [
    path('atracao/update/<int:pk>', AtracaoUpdateView.as_view() , name="atracao_update"),
    path('atracao/create/', AtracaoCreateView.as_view() , name="atracao_create"),
    path('atracao/delete/<int:pk>', AtracaoDeleteView.as_view() , name="atracao_delete"),
    path('atracao/<int:pk>', AtracaoDetailsView.as_view() , name="atracao_detail"),
    path('atracao/list/', AtracaoListView.as_view(), name="atracao_list"),

    #path('register/', UserCreateViewGeneric.as_view() , name="register"),
]
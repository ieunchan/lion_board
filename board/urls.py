from django.urls import path
from .views import test, test1, ItemLV,ItemDV,ItemCV,itemLV

urlpatterns = [
    path('', ItemLV.as_view(), name='index'),
    path('detail/<int:pk>', ItemDV.as_view(), name='detail'),
    path('create/', ItemCV.as_view(), name='create'),
    path('lion/', test),
    path('lion/<int:pk>', test1),
    path('f/', itemLV),
]
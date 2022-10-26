from django.urls import path
from .views import *
urlpatterns = [
    path('' , index , name='index'),
    path('getTimer/' , getTimer , name = 'get timer'),
    path('roll/' , roll  , name = 'roll')
]
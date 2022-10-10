from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('genral',views.genral,name='genral'),
    path('business',views.business,name='business'),
    path('sport',views.sport,name='sport'),
    path('technology',views.technology,name='technology'),
    path('entertainment',views.entertainment,name='entertainment'),
    
]
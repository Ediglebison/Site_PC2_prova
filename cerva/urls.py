from django.urls import URLPattern, path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('historia', views.historia, name='historia'),
    path('escolas', views.escolas, name='escolas'),
    path('alema', views.alema, name='alema'),
    path('inglesa', views.inglesa, name='inglesa'),
    path('belga', views.belga, name='belga'),
    path('americana', views.americana, name='americana'),
    path('pureza', views.pureza, name='pureza'),
    path('cerveja', views.cerveja, name='cerveja'),
    path('harmonizacao', views.harmonizacao, name='harmonizacao'),
    path('fabricacao', views.fabricacao, name='fabricacao')
    
]
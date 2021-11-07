from django.conf.urls import url
from django.urls import path
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.get_calculation),
    path('api/moves', views.MoveView.as_view()),
    path('api/pokemon', views.PokemonView.as_view()),
    path('api/items', views.ItemView.as_view())   # This line has changed!
]


from django.urls import path
import quotes.views as views

app_name = 'quotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('top/', views.top, name='topQuotes'),
    path('add/', views.add, name='add'),
    path('like/<int:quoteId>/', views.like, name='like'),
    path('dislike/<int:quoteId>/', views.dislike, name='dislike'),
]

from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('new/<int:n>', views.new, name='new'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contact'),
    path('sidebar/', views.sidebar),
    path('registration/', views.registration, name='registration'),
    path('user_account/', views.user_account, name='user_account'),
    path('about/', views.about, name='about'),
]
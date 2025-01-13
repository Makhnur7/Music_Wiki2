from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.group_list, name='group_list'),
    path('albums/', views.album_list, name='album_list'),
    path('songs/', views.song_list, name='song_list'),
    path('members/', views.member_list, name='member_list'),
    path('group/<int:pk>/', views.group_detail, name='group_detail'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
]



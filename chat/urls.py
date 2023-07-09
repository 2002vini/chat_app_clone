from django.urls import path
from . import views



app_name = 'chat'


urlpatterns = [
    # path('', views.ChatAPI.as_view(), name="ChatAPI"),
    # path('direct/<uuid:receiver_id>/', views.ChatAPI.as_view(), name="directMessage"),

    path('', views.index, name="index"),
    path('direct/<uuid:receiver_id>/', views.directMessage, name="directMessage"),
    path('group/', views.createGroup, name="createGroup"),
    path('group/<str:group_id>/', views.groupMessage, name="groupMessage"),
    #path('search/',views.search,name='search'),
    path('search/',views.usersearch.as_view(),name='search'),
    path('roles/<str:role>/',views.Display.as_view()),
    path('form',views.FormAPIView.as_view()),
    path('friend-request',views.FriendRequestAPIView.as_view()),
    path('friend-request/<uuid:receiver_id>/',views.FriendRequestAPIView.as_view(),name='createRequest'),
   
]
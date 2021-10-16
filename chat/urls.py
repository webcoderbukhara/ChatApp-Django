from django.urls import path
from .views import room_view,create_room, room
urlpatterns = [
    path('room_view/',room_view,name='room_view'),
    path('create_room/',create_room,name='create_room'),
    path('room_view/room/<str:room_name>/',room,name='room'),


# http://127.0.0.1:8000/chat/room_view/room_view1/room/1/
#  return redirect('room_view'+'/room/'+str(room_name)+"/") 
    
    
]
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Human,Room, Message
# Create your views here.

def room_view(request):
    context = {}
    human = request.user
    room = Room.objects.all()
    context['human'] = human
    context['room'] = room
    humen = Human.objects.filter(user=human)

    if request.method == 'POST':
        room_name = request.POST.get("room_name")
        room_1 =(Room.objects.get(name=room_name))
        room_1.humen.add(*humen)
        print(room_1.humen)
        # for hum in Room.objects.filter(name=room_name):
        #     hum.humen.user.add(human)
        #     hum.humen.filter(name=room_name).delete()
        

        


       
        
    
        
        return redirect('room/'+str(room_1.name)+"/") 

    return render(request,'chat/room.html',context)
def create_room(request):
    human = Human.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        humans = request.POST.get('human')

        rom = Room.objects.filter(name=name)   
        if len(rom)==0:         
         room = Room(name=name)
         room.save()
         return redirect('room_view')
        # for hum in Room.objects.filter(name=name):
        #     hum.humen.add(*humans)
        else:
         return render(request,'chat/room_create.html',{'err':'Bu nomdagi chat mavjud','human':human})


         
        

    
    return render(request,'chat/room_create.html',{'human':human})
    
def room(request,room_name):
    context={}    

    room_name = Room.objects.filter(name=room_name)[0]
    context['room_name'] = room_name
    print(room_name)
    message = Message.objects.filter(room=room_name).order_by('-created')
    context['message'] = message
    human = Human.objects.filter(user=request.user)[0]
    context['human_name'] = human.user.username
    if request.method=='POST':
        content = request.POST.get('message')
        if (content) != '' and len(content)!=0:
            new_message = Message(content=content,human=human,room=room_name)
           
            new_message.save()
        content = ''

    
    return render(request,'chat/room_chat.html',context)


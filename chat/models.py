from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Human(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='avatar/', default='avatar/img_avatar2.png')

    def __str__(self):
        return self.user.username
    

class Room(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='room_images/',default='room_images/img_coffee.jpg' )
    humen = models.ManyToManyField(Human)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    content = models.TextField()
    human = models.ForeignKey(Human,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room

# class Human_Message(models.Model):
#     content = models.TextField()
#     user1 = models.ForeignKey(Human,on_delete=models.CASCADE)
#     human = models.ForeignKey(Human,on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.human
from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CASCADE, DateTimeField, TextField

from apps.room.models import Room


class Message(Model):
    room = ForeignKey(Room, related_name='messages', on_delete=CASCADE)
    user = ForeignKey(User, related_name='messages', on_delete=CASCADE)
    content = TextField()
    date_added = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
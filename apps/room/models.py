from django.db.models import CharField, SlugField, Model


class Room(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

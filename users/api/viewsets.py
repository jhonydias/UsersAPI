from rest_framework import viewsets
from users import models
from users.api import serializers

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = models.Users.objects.all()
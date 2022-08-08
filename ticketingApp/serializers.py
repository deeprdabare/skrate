from rest_framework import serializers 
from ticketingApp.models import User, Ticket
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'is_staff',
                  'role')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('title',
                  'description',
                  'assignedTo',
                  'status',
                  'priority')

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',
                  'created',
                  'user_id')

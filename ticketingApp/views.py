from django.shortcuts import render
from django.http.response import JsonResponse
from django.core import serializers
from django.http import QueryDict

from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
 
from ticketingApp.models import User, Ticket
from ticketingApp.serializers import UserSerializer, TicketSerializer, TokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

@api_view(['POST'])
@permission_classes([AllowAny])
def user_new(request):
    userdetails = JSONParser().parse(request)

    if(userdetails['role'] == 'admin'):
        userdetails['is_staff'] = True
    elif(userdetails['role'] == 'employee'):
        userdetails['is_staff'] = False
    else:
        return JsonResponse({"message":"Invalid role !"},
                            status=status.HTTP_400_BAD_REQUEST)
        
    user_serializer = UserSerializer(data=userdetails)

    if user_serializer.is_valid():
        user = user_serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key},
                            status=status.HTTP_201_CREATED)
    return JsonResponse(user_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def users_list(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False,
                        status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def tickets_new(request):
    ticketdetails = JSONParser().parse(request)

    try:
        user = User.objects.get(id=ticketdetails['assignedTo'])
        ticketdetails['assignedTo'] = int(user.id)
    except:
        JsonResponse({"message":"Invalid user id !"},
                            status=status.HTTP_400_BAD_REQUEST)
    
    ticket_serializer = TicketSerializer(data=ticketdetails)

    if ticket_serializer.is_valid():
        ticket = ticket_serializer.save()
        return JsonResponse(ticket_serializer.data,
                            status=status.HTTP_201_CREATED)
    return JsonResponse(ticket_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tickets_list(request):
    tickets = list(Ticket.objects.values())
    return JsonResponse(tickets, safe=False,
                        status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tickets_params(request):
    tstatus = request.query_params.get('status', None)
    title = request.query_params.get('title', None)
    priority = request.query_params.get('priority', None)

    if tstatus != None:
        tickets = serializers.serialize('json', Ticket.objects.filter(status=tstatus))
        return JsonResponse(tickets, safe=False,
                            status=status.HTTP_201_CREATED)
    if title != None:
        tickets = serializers.serialize('json', Ticket.objects.filter(title=title))
        return JsonResponse(tickets, safe=False,
                            status=status.HTTP_201_CREATED)
    if priority != None:
        tickets = serializers.serialize('json', Ticket.objects.filter(priority=priority))
        return JsonResponse(tickets, safe=False,
                            status=status.HTTP_201_CREATED)

    return JsonResponse({"message":"Invalid parameter !"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def tickets_close(request):
    token = Token.objects.get(key = request.META.get('HTTP_AUTHORIZATION').replace('Token ',''))
    user = User.objects.get(username = token.user)
    
    closed = {"status" : Ticket.TicketStatus.CLOSE}
    tid = request.data.get('ticketid')
    ticket = Ticket.objects.get(id = tid)
    #ticket.status = "close"

    if ticket.assignedTo == user.id or user.is_staff:
        ticket_serializer = TicketSerializer(ticket, data=closed, partial = True)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            return JsonResponse(ticket_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message":"Unauthorized !"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def tickets_delete(request):
    tid = request.data.get('ticketid')

    try:
        ticket = Ticket.objects.get(id = tid)
        ticket.delete()
        return JsonResponse({"message":"Ticket deleted"}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def see_all_tokens(request):
    tokens = Token.objects.get(key = request.META.get('HTTP_AUTHORIZATION').replace('Token ',''))
    return JsonResponse({"tokens" : tokens})
    token_serializer = TokenSerializer(data = tokens)
    if token_serializer.is_valid():
        return JsonResponse(tokens, safe = False, status=status.HTTP_201_CREATED)
    return JsonResponse(token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@permission_classes([AllowAny])
def test_request(request):
    return JsonResponse({"message":"Pong !!"}, status=status.HTTP_201_CREATED)




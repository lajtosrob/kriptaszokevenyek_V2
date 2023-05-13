from django.shortcuts import render

from django.http import JsonResponse
from .models import PlayerCharacter
from .serializers import PlayerCharacterSerializer


def getPlayer(request, id):
    actulCharachter = PlayerCharacter.objects.get(id=id)
    
    serializedCharacter = PlayerCharacterSerializer(actulCharachter,
    many = False)
    # serializedCharacter = { 
    #       "name" : actulCharachter.name,
    #       "health" : actulCharachter.health, 
    #       "attak" : actulCharachter.attak,
    #       "defense": actulCharachter.defense,
    #       "luck" : actulCharachter.luck,
    #       "magic" : actulCharachter.magic,     
    # }
    return JsonResponse(serializedCharacter.data)


# Create your views here.

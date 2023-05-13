from rest_framework import serializers
from .models import PlayerCharacter

class PlayerCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCharacter  # jelenleg a játékoskaraktert akajuk lekérdezni
        fields = '__all__'  #   a karakterről minden adatot...
        
        # lehet ilyen lekérdezés is pl --> ['name', 'image']
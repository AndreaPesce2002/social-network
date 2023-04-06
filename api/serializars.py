from rest_framework import serializers
from frontend.models import Utente, Post

class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = ['id', 'nome', 'descrizione', 'followers', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['num_follower'] = instance.num_follower()
        return representation


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['time_passed'] = instance.time_passed()
        return representation

    def update_with_like(self, instance, validated_data):
        instance.add_like()
        return instance
from rest_framework import serializers
from .models import UserProfile, Hotel, Room, Booking


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profiles"""

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}

                }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Update and return an existing user"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class HotelSerializer(serializers.ModelSerializer):
    """Serializer for hotels"""

    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    """Serializer for rooms"""

    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for bookings"""

    class Meta:
        model = Booking
        fields = '__all__'

from rest_framework import serializers
from .models import Audiobook, Chapter, Favorite, Author, Narrator, Publisher, User
from django.contrib.auth.password_validation import validate_password

# User serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'profile_pic']
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'profile_pic']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            profile_pic=validated_data.get('profile_pic')
        )
        return user

# Audiobook and Chapter serializers
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class AudiobookSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField()
    narrator = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()

    class Meta:
        model = Audiobook
        fields = '__all__'

# Favorite serializer (single model handling all favorites)
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

# Author, Narrator, Publisher serializers
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class NarratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Narrator
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

# Optional: Specific Favorite serializers can be kept, if needed
class FavoriteAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'author']

class FavoriteNarratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'narrator']

class FavoritePublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'publisher']

from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', 'data_register')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language']


class RatingSerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()

    class Meta:
        model = Rating
        fields = ['user', 'stars']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    year =serializers.DateField(format('%m-%d-%Y'))

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image', 'year',
                  'country', 'genre', 'status_movie']

class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    year =serializers.DateField(format('%m-%d-%Y'))
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    prop = MovieLanguagesSerializer(many=True, read_only=True)
    moments = MomentsSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image', 'year',
                  'country', 'genre', 'director', 'actor',
                  'movie_time', 'description', 'movie_trailer', 'status_movie', 'prop', 'moments']


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    favorite_movies = FavoriteMovieSerializer(many=True, read_only=True, source='favoritemovie_set')

    class Meta:
        model = Favorite
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']
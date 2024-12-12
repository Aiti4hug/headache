from django_filters import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'movie_name': ['exact'],
            'year': ['gt', 'lt'],
            'director': ['exact'],
            'actor': ['exact'],
            'genre': ['exact'],
            'status_movie': ['exact']
        }
from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name',)

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name',)

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)
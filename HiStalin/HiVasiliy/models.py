from datetime import datetime
from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='age', null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(80)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    data_register = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Country(models.Model):
    country_name = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return f'{self.country_name}'

class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio =models.TextField()
    age = models.PositiveSmallIntegerField(verbose_name='age', null=False, blank=False,
                                           validators=[MinValueValidator(18), MaxValueValidator(80)])
    director_image = models.ImageField(upload_to='director_images/', null=False, blank=False)


    def __str__(self):
        return f'{self.director_name}, {self.age}'


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(verbose_name='age', null=False, blank=False,
                                           validators=[MinValueValidator(18), MaxValueValidator(80)])
    actor_image = models.ImageField(upload_to='actor_images/', null=True, blank=True)


    def __str__(self):
        return f'{self.actor_name}, {self.age}'

class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)


    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=80)
    year = models.DateField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor, related_name='actor_films')
    genre = models.ManyToManyField(Genre)
    TYPES_CHOICES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p')
    )
    types = MultiSelectField(max_length=16, choices=TYPES_CHOICES, max_choices=5)
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailer/')
    movie_image = models.ImageField(upload_to='movie_images/')
    status_movie = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simple')


    def __str__(self):
        return f'{self.movie_name}, {self.year}'

    def get_avg_rating(self):
        rating = self.ratings.all()
        if rating.exists():
            return round(sum(i.stars for i in rating) / rating.count(), 1)
        return 0


class MovieLanguages(models.Model):
    language = models.CharField(max_length=32, verbose_name='Язык')
    video = models.FileField(upload_to='movie_languages/', null=False, blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_moments')

    def __str__(self):
        return self.language


class Moments(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  movie_moment = models.FileField(upload_to='movie_moments/', null=False, blank=False, verbose_name='Кадры момента')

  def __str__(self):
      return f'Moment from {self.movie.movie_name}'

class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models .IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    text = models.TextField(max_length=500)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.movie.movie_name} ({self.stars} stars)"


class Favorite(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')


    def __str__(self):
        return f'{self.user}'

class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return f'FavoriteMovie: {self.cart}'

class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')


    def __str__(self):
        return f'{self.movie}, {self.viewed_at}'
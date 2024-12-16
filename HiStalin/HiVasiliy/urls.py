from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'movie_list', MovieListViewSet, basename='movie_list')
router.register(r'movie_detail', MovieDetailViewSet, basename='movie_detail')
router.register(r'user', UserProfileViewSet, basename='user')
router.register(r'director', DirectorViewSet, basename='director')
router.register(r'actor', ActorViewSet, basename='actors')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'favorite_movie', FavoriteMovieViewSet, basename='favorite_movie')
router.register(r'history', HistoryViewSet, basename='history')
router.register(r'rating', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls))
]

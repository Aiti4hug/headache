from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', MovieViewSet.as_view({'get': 'list',
                                   'post': 'create'}), name='movie_list'),

    path('<int:pk>/', MovieViewSet.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'delete': 'destroy'}), name='movie_detail'),


    path('user/', UserProfileViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='user_list'),

    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'}), name='user_detail'),


    path('country/', CountryViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='country'),

    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='country_detail'),


    path('directory/', DirectoryViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='directory'),

    path('directory/<int:pk>/', DirectoryViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='directory_detail'),


    path('actor/', ActorViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='actor'),

    path('actor/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='actor_detail'),


    path('genre/', GenreViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='genre'),

    path('genre/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='genre_detail'),


    path('movielanguages/', MovieLanguagesViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='movielanguages'),

    path('movielanguages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='movielanguages_detail'),


    path('rating/', RatingViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='rating_list'),

    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='rating_detail'),


    path('moments/', MomentsViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='moments'),


    path('favorite/', FavoriteViewSet.as_view({'get': 'list',
                                               'post': 'create'}), name='favorite_list'),

    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve',
                                                        'put': 'update',
                                                        'delete': 'destroy'}), name='favorite_detail'),

    path('favoritemovie/', FavoriteMovieViewSet.as_view({'get': 'list',
                                                          'post': 'create'}), name='favorite_movie_list'),

    path('favoritemovie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve',
                                                                   'put': 'update',
                                                                   'delete': 'destroy'}), name='favorite_movie_detail'),


    path('history/', HistoryViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='history_list'),

    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='history_detail'),
]
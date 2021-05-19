from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import VideoViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)

urlpatterns = [    
    #path('api/', include('youtubeapi.urls')),
    path('', include(router.urls)),
]
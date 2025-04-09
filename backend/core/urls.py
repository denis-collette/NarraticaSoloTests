from django.urls import path, include
from .views import RegisterView, LoginView, AudiobookViewSet, ChapterViewSet, FavoriteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'audiobooks', AudiobookViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]

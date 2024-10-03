from django.urls import path, include
from bookings import views
from .views import UserProfileViewSet, HotelViewSet, RoomViewSet, BookingViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('hotels', HotelViewSet)
router.register('rooms', RoomViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

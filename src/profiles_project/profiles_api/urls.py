from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

# routers for the viewsets
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)  # no base name because it's a ModelViewSet
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
]

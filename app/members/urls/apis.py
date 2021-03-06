from django.urls import path, re_path

from ..apis import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    UserLoginAuthTokenAPIView, UserLogoutView
)

urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),

    path('login/', UserLoginAuthTokenAPIView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]

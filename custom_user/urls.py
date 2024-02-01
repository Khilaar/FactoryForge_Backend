from django.urls import path
from .views import UserSingleView, UserListCreateUserView, RetrieveUpdateDeleteUserView, CurrentUserView, \
    CurrentUserUpdateView

urlpatterns = [
    path("", UserListCreateUserView.as_view()),
    path('<int:pk>/', UserSingleView.as_view(), name='user-detail'),
    path("patch/<int:pk>/", RetrieveUpdateDeleteUserView.as_view(), name='user-patch'),
    path("delete/<int:pk>/", RetrieveUpdateDeleteUserView.as_view(), name='user-delete'),
    path("me/", CurrentUserView.as_view(), name='current-user'),
    path('me/update/', CurrentUserUpdateView.as_view(), name='user-update'),
]
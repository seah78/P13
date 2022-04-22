from django.urls import path

from profiles.views import profile, profiles_index

urlpatterns = [
    path("", profiles_index, name="profiles_index"),
    path("<str:username>/", profile, name="profile"),
]

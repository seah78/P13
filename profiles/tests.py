from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from profiles.models import Profile


class TestIndex(TestCase):
    def test_index(self):
        client = Client()

        response = client.get(reverse("profiles:profiles_index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Profiles</title>")
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_context(self):
        client = Client()
        wrong_user = User.objects.create(username="SEAH")
        Profile.objects.create(user=wrong_user, favorite_city="Chocques")

        response = client.get(reverse("profiles:profile", kwargs={"username": "SEAH"}))
        self.assertContains(response, "<title>SEAH</title>")
        self.assertContains(response, "<p>Favorite city: Chocques</p>")

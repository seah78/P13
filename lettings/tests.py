from django.test import Client, TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class TestIndex(TestCase):
    def test_index(self):
        client = Client()

        response = client.get(reverse("lettings:lettings_index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Lettings</title>')
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_context(self):
        client = Client()
        wrong_address = Address.objects.create(
            number="16",
            street="Rue Louis Delalleau",
            city="Chocques",
            state="FR",
            zip_code="62920",
            country_iso_code="FRA",
        )
        Letting.objects.create(title="Wrong Letting", address=wrong_address)

        response = client.get(reverse("lettings:letting", kwargs={"letting_id": 1}))
        self.assertContains(response, '<title>Wrong Letting</title>')
        self.assertContains(response, '<p>16 Rue Louis Delalleau</p>')

from django.test import TestCase, Client
from django.urls import reverse
from .models import donor_Registration, con_tact


class BloodBankTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.donor = donor_Registration.objects.create(
            name="Rahim Uddin",
            father_name="Karim Uddin",
            gender="male",
            email="rahim@example.com",
            phone_number="01712345678",
            state="Dhaka",
            city="Uttara",
            blood_group="o-",
            occupation="Engineer",
            home_address="Sector 10, Uttara",
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_search_page_and_filter(self):
        response = self.client.post(reverse('search_list'), {
            'blood_group': 'o-',
            'state': 'Dhaka',
            'city': 'Uttara'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahim Uddin")

    def test_search_info_by_id(self):
        response = self.client.get(reverse('search_info', args=[self.donor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahim Uddin")

    def test_contact_form(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'phone_number': '01812345678',
            'email': 'test@example.com',
            'subject': 'Need urgent blood'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(con_tact.objects.count(), 1)

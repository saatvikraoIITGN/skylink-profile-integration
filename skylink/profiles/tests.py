from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Profile

# Create your tests here 

class ProfileTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.profile_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'address': '123 Main St',
            'tmc_id': 'TMC123',
            'date_of_birth': '1980-01-01'
        }
        self.response = self.client.post(
            '/api/profiles/',
            self.profile_data,
            format='json'
        )
        self.profile = Profile.objects.get()

    def test_create_profile(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().first_name, 'John')

    def test_get_profile(self):
        response = self.client.get(f'/api/profiles/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')

    def test_update_profile(self):
        update_data = {'first_name': 'Jane'}
        response = self.client.patch(f'/api/profiles/{self.profile.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, 'Jane')

    def test_delete_profile(self):
        response = self.client.delete(f'/api/profiles/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.count(), 0)

    def test_create_profile_missing_fields(self):
        invalid_data = {
            'first_name': 'John',
            'last_name': 'Kirk',
        }
        response = self.client.post('/api/profiles/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_nonexistent_profile(self):
        response = self.client.get('/api/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_update_nonexistent_profile(self):
    #     update_data = {'first_name': 'Jane'}
    #     response = self.client.patch('/api/profiles/999/', update_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_delete_nonexistent_profile(self):
    #     response = self.client.delete('/api/profiles/999/')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
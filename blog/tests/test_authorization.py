from rest_framework.test import APITestCase
from rest_framework import status


class TestUserAuth(APITestCase):

    def test_signup(self):
        data = {'username': 'qwerty', 'password': 'qwerty098765'}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {'username': 'qwerty', 'password': 'qwerty098765'}
        self.client.post('/api/users/', data)
        response = self.client.post('/auth/token/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        data = {'username': 'qwerty', 'password': 'qwerty098765'}
        response = self.client.post('/auth/token/logout', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_users_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

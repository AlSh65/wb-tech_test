from rest_framework.test import APITestCase
from rest_framework import status


class TestPost(APITestCase):
    def test_post_create(self):
        post_data = {'title': 'post title ', 'text': 'post text'}
        response = self.client.post('/api/post/', post_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_list(self):
        response = self.client.get('/api/post/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

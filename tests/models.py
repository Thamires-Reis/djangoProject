from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='usertest',
            email='usertest@example.com',
            password='passwordtest'
        )

    def test_login(self):
        #POST request for the login view with valid credentials
        response = self.client.post(reverse('login'), {
            'username': 'usertest',
            'password': 'passwordtest'
        })
        # Verify the response status (redirect)
        self.assertEqual(response.status_code, 302)
        ## Make sure the response redirects to the home page.
        self.assertEqual(response.url, reverse('home'))

    def test_login_with_invalid_credentials(self):
        #POST request for the login view with invalid credentials
        response = self.client.post(reverse('login'), {
            'username': 'usertest',
            'password': 'incorrectpassword'
        })
        # Verify the response status (OK)
        self.assertEqual(response.status_code, 200)
        # Verify that the response includes the error message.
        self.assertContains(response, 'Please enter a correct username and password.')


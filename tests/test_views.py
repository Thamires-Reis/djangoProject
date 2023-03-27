from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class LoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='usertest',
            password='passtest'
        )

    # Ensures that the login page loads successfully and that the correct template is used.
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    # Ensures that a user can log in successfully using valid credentials, and is redirected to the home page.
    def test_login_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'usertest',
            'password': 'passtest'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    # Ensures that a user cannot log in using invalid credentials, and sees an error message displayed on the login
    # page.
    def test_login_failure(self):
        response = self.client.post(reverse('login'), {
            'username': 'incorrectuser',
            'password': 'incorrectpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'Please enter a correct username and password.')

from django.test import TestCase, Client
from django.conf import settings
from .models import Link
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class LinkModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Alex',
            email='test@test.com',
            password='testtesttest'
        )

        link1 = Link.objects.get_or_create(
            user=user,
            link='http://google.com',
            comment='test'
            )

        link2 = Link.objects.get_or_create(
            user=user,
            link='http://yandex.com',
            comment='yandex'
            )
        self.user = user

    def test_get_url(self):
        links = Link.objects.filter(user=self.user).order_by('date')
        self.assertEqual(links[0].get_absolute_url(), 'http://google.com')
        self.assertEqual(links[1].get_absolute_url(), 'http://yandex.com')


class LinksListTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Alex',
            email='test@test.com',
            password='testtesttest'
        )

        link1 = Link.objects.get_or_create(
            user=user,
            link='http://google.com',
            comment='test'
            )

        link2 = Link.objects.get_or_create(
            user=user,
            link='http://yandex.com',
            comment='yandex'
            )

        self.client = Client()

        self.url = reverse('links:list')
        self.user = user

    def test_list_links(self):
        links = Link.objects.filter(user=self.user).order_by('date')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(links[0].get_absolute_url(), response.content.decode('utf8'))
        self.assertIn(links[1].get_absolute_url(), response.content.decode('utf8'))
        self.assertEqual(len(response.context['links']), 2)


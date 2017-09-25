# -*- coding: utf-8 -*-

from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase


class ChannelViewSetTests(APITestCase):

    def test_list_channels(self):
        """Test endpoint which lists all channels."""

        channel_1 = mommy.make("Channel", name="WALMART")
        channel_2 = mommy.make("Channel", name="SUBMARINO")

        channels = [{"id": str(channel_1.id), "name": channel_1.name},
                    {"id": str(channel_2.id), "name": channel_2.name}]

        url = reverse('core-api:channel-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(channels, response.data)

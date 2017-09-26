# -*- coding: utf-8 -*-

from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from apps.core.api.serializer import ChannelListSerializer, ChannelDetailSerializer, \
    CategoryListSerializer, CategoryDetailSerializer


class ChannelViewSetTests(APITestCase):
    def test_list_all_channels(self):
        """Test whether 'core-api:channel-list' lists all existing channels."""

        channels = [mommy.make("Channel") for _ in range(10)]

        serializer = ChannelListSerializer(instance=channels, many=True)

        url = reverse('core-api:channel-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(serializer.data, response.data)

    def test_retrieve_channel_details(self):
        """Test whether 'core-api:channel-detail' retrieves the correct channel."""

        channel = mommy.make("Channel")

        serializer = ChannelDetailSerializer(instance=channel)

        url = reverse('core-api:channel-detail', args=[channel.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)


class CategoryViewSetTests(APITestCase):
    def test_list_all_categories(self):
        """Test whether 'core-api:category-list' list all existing categories."""

        categories = [mommy.make("Category") for _ in range(10)]

        serializer = CategoryListSerializer(instance=categories, many=True)

        url = reverse('core-api:category-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(serializer.data, response.data)

    def test_retrieve_category_details(self):
        """Test whether 'core-api:category-detail' retrieves the correct category."""

        category = mommy.make("Category")

        serializer = CategoryDetailSerializer(instance=category)

        url = reverse('core-api:category-detail', args=[category.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

# -*- coding: utf-8 -*-

from django.test import TestCase
from model_mommy import mommy

from apps.core.api.serializer import ChannelSerializer, CategorySerializer


class ChannelSerializerTest(TestCase):
    def test_channel_serialization(self):
        """Test whether channel serialization was well succeed."""

        channel = mommy.make("Channel")
        serializer = ChannelSerializer(channel)

        self.assertCountEqual(serializer.data.keys(), ["id", "name"])
        self.assertCountEqual(serializer.data.values(), [str(channel.id), channel.name])

    def test_max_length_channel_name(self):
        """Test max_length constraint in channel's name field."""

        serializer_data = {"name": "a" * 61}
        serializer = ChannelSerializer(data=serializer_data)

        self.assertFalse(serializer.is_valid())
        self.assertCountEqual(serializer.errors.keys(), ["name"])


class CategorySerializerTest(TestCase):
    def test_category_serialization(self):
        """Test whether category serialization was well succeed."""

        self.channel = mommy.make("Channel")
        self.node_1 = mommy.make("Category")
        self.node_2 = mommy.make("Category", parent_category=self.node_1)
        self.node_3 = mommy.make("Category", parent_category=self.node_2)

        serializer = CategorySerializer(self.node_2)

        self.assertCountEqual(
            serializer.data.keys(), ["id", "name", "channel", "parents", "subcategories"]
        )

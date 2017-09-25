# -*- coding: utf-8 -*-

from django.test import TestCase
from model_mommy import mommy

from apps.core.api.serializer import ChannelSerializer


class ChannelSerializerTest(TestCase):
    def test_channel_serialization(self):
        """Test wether channel serialization was well succeed."""

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

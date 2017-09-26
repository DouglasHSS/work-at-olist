# -*- coding: utf-8 -*-

from django.test import TestCase
from model_mommy import mommy

from apps.core.api.serializer import ChannelListSerializer, ChannelDetailSerializer, \
    CategoryListSerializer, CategoryDetailSerializer


class ChannelListSerializerTest(TestCase):

    def test_contain_expected_attributes(self):
        """Test whether a serialized channel has the expected attributes"""

        channel = mommy.make("Channel")
        serializer = ChannelListSerializer(channel)

        self.assertCountEqual(serializer.data.keys(), ["id", "name"])


class CategoryListSerializerTest(TestCase):
    def test_contain_expected_attributes(self):
        """Test whether a serialized category contains the expected attributes"""

        category = mommy.make("Category")
        serializer = CategoryListSerializer(category)

        self.assertCountEqual(
            serializer.data.keys(), ["id", "name", "channel", "parent_categories", "subcategories"]
        )


class ChannelDetailSerializerTest(TestCase):
    def test_contain_expected_attributes(self):
        """Test whether a serialized channel contains the expected attributes"""

        channel = mommy.make("Channel")
        serializer = ChannelDetailSerializer(channel)

        self.assertCountEqual(serializer.data.keys(), ["id", "name", "categories"])


class CategoryDetailSerializerTest(TestCase):
    def test_contain_expected_attributes(self):
        """Test whether a serialized category contains the expected attributes"""

        category = mommy.make("Category")
        serializer = CategoryDetailSerializer(category)

        self.assertCountEqual(serializer.data.keys(), ["name", "all_subcategories"])

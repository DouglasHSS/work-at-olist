# -*- coding: utf-8 -*-

from django.test import TestCase
from model_mommy import mommy


class ChannelTest(TestCase):
    def test_str_method(self):
        """Test printable string representation of a Channel object."""
        channel = mommy.make("Channel")
        self.assertEqual(str(channel), channel.name)

    def test_create_channel(self):
        mommy.make("Channel")


class CategoryTest(TestCase):
    def test_str_method(self):
        """Test printable string representation of a Category object."""
        channel = mommy.make("Channel")
        category = mommy.make("Category", channel=channel)

        str_ = "{channel_name} - {category_name}".format(
            channel_name=category.channel.name,
            category_name=category.name
        )

        self.assertEqual(str(category), str_)

    def test_create_category(self):
        mommy.make("Category")

    def test_check_path(self):
        """Test category path till its root parent category."""
        node_1 = mommy.make("Category")
        node_2 = mommy.make("Category", parent_category=node_1)
        node_3 = mommy.make("Category", parent_category=node_2)

        path_1 = [node_1]
        path_2 = [node_1, node_2]
        path_3 = [node_1, node_2, node_3]

        self.assertEqual(path_1, node_1.path)
        self.assertEqual(path_2, node_2.path)
        self.assertEqual(path_3, node_3.path)

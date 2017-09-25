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

    def test_check_parents(self):
        """Test previous parents of a single category."""
        node_1 = mommy.make("Category", name="1")
        node_2 = mommy.make("Category", name="2", parent_category=node_1)
        node_3 = mommy.make("Category", name="3", parent_category=node_2)

        parents_node_1 = []
        parents_node_2 = [node_1]
        parents_node_3 = [node_1, node_2]

        self.assertEqual(parents_node_1, node_1.parents)
        self.assertEqual(parents_node_2, node_2.parents)
        self.assertEqual(parents_node_3, node_3.parents)

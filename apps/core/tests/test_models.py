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
        category = mommy.make("Category")

        self.assertEqual(str(category), category.name)

    def test_create_category(self):
        mommy.make("Category")

    def test_check_parent_categories(self):
        """Test previous parent_categories of a single category."""
        category_1 = mommy.make("Category", name="1")
        category_2 = mommy.make("Category", name="2", parent_category=category_1)
        category_3 = mommy.make("Category", name="3", parent_category=category_2)

        parent_categories_1 = []
        parent_categories_2 = [category_1]
        parent_categories_3 = [category_1, category_2]

        self.assertEqual(parent_categories_1, category_1.parent_categories)
        self.assertEqual(parent_categories_2, category_2.parent_categories)
        self.assertEqual(parent_categories_3, category_3.parent_categories)

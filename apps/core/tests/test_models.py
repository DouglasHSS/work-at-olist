# -*- coding: utf-8 -*-

from django.test import TestCase
from model_mommy import mommy


class ChannelTest(TestCase):
    def test_str_method(self):
        """Test printable string representation of a Channel object."""

        channel = mommy.make("Channel")
        self.assertEqual(str(channel), channel.name)

    def test_contain_expected_root_categories(self):
        """Test whether a channel contains the expected root categories."""

        channel = mommy.make("Channel")

        category_1 = mommy.make("Category", channel=channel)
        category_2 = mommy.make("Category", channel=channel, parent_category=category_1)
        category_3 = mommy.make("Category", channel=channel)

        self.assertCountEqual(channel.categories.all(), [category_1, category_2, category_3])
        self.assertCountEqual(channel.root_categories.all(), [category_1, category_3])


class CategoryTest(TestCase):
    def test_str_method(self):
        """Test printable string representation of a Category object."""

        category = mommy.make("Category")
        self.assertEqual(str(category), category.name)

    def test_check_parent_categories(self):
        """Test previous parent_categories of a single category."""

        category_1 = mommy.make("Category")
        category_2 = mommy.make("Category", parent_category=category_1)
        category_3 = mommy.make("Category", parent_category=category_2)

        parent_categories_1 = []
        parent_categories_2 = [category_1]
        parent_categories_3 = [category_1, category_2]

        self.assertEqual(parent_categories_1, category_1.parent_categories)
        self.assertEqual(parent_categories_2, category_2.parent_categories)
        self.assertEqual(parent_categories_3, category_3.parent_categories)

    def test_check_all_subcategories_(self):
        """Test whether property all_subcategories in fact returns all subcategories."""

        category = mommy.make("Category")
        mommy.make("Category", parent_category=category)
        mommy.make("Category", parent_category=category)

        self.assertCountEqual(category.subcategories.all(), category.all_subcategories)

# -*- coding: utf-8 -*-

from django.test import TestCase
from model_mommy import mommy


class ChannelTest(TestCase):

    def test_str_method(self):
        channel = mommy.make("Channel")
        self.assertEqual(str(channel), channel.name)

    def test_create_channel(self):
        mommy.make("Channel")


class CategoryTest(TestCase):

    def test_str_method(self):
        channel = mommy.make("Channel")
        category = mommy.make("Category", channel=channel)

        str_ = "{channel_name} - {category_name}".format(
            channel_name=category.channel.name,
            category_name=category.name
        )

        self.assertEqual(str(category), str_)

    def test_create_category(self):
        mommy.make("Category")

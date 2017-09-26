# -*- coding: utf-8 -*-
import os

from django.test import TestCase
from django.core.management import call_command
from model_mommy import mommy

from django.conf import settings
from apps.core.models import Channel


class ImportCategoriesCommandTest(TestCase):

    def setUp(self):
        self.csv_path = os.path.join(settings.BASE_DIR, "csv_sample/channels_categories.csv")

    def test_create_new_channel(self):
        """Test of new channel creation."""

        channel_name = "WALMART"

        channels = Channel.objects.filter(name=channel_name)
        self.assertFalse(channels.exists())

        call_command("import_categories", channel_name, self.csv_path)

        channel = Channel.objects.get(name=channel_name)

        self.assertEqual(channel.name, channel_name)

    def test_keep_existing_channel(self):
        """Test of keeping existing_channel."""

        channel_name = "WALMART"
        channel_1 = mommy.make("Channel", name=channel_name)

        call_command("import_categories", channel_name, self.csv_path)
        channels = Channel.objects.filter(name=channel_name)
        self.assertEqual(1, channels.count())

        channel_2 = channels.first()
        self.assertEqual(channel_1, channel_2)

    def test_create_all_channels_categories(self):
        """Test creation of all channel's categories."""

        channel_name = "WALMART"
        call_command("import_categories", channel_name, self.csv_path)

        channel = Channel.objects.get(name=channel_name)
        self.assertEqual(23, channel.categories.count())

    def test_create_root_categories(self):
        """Test creation of channel's root categories."""

        channel_name = "WALMART"
        call_command("import_categories", channel_name, self.csv_path)

        channel = Channel.objects.get(name=channel_name)
        root_categories = channel.categories.filter(parent_category__isnull=True)

        self.assertEqual(3, root_categories.count())

    def test_create_leaf_categories(self):
        """Test creation of channel's leaf categories."""

        channel_name = "WALMART"
        call_command("import_categories", channel_name, self.csv_path)

        channel = Channel.objects.get(name=channel_name)
        leaf_categories = channel.categories.filter(subcategories__isnull=True)

        self.assertEqual(16, leaf_categories.count())

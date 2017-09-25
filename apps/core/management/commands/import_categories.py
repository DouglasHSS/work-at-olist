# -*- coding: utf-8 -*-

import csv

from django.core.management.base import BaseCommand

from apps.core.models import Channel, Category


class Command(BaseCommand):
    help = "Import all channel's categories from a csv file."

    def _create_channel(self, channel_name):
        """Create a new channel in case it does not exist.

        :param channel_name: Name of the channel which is being imported.
        :type channel_name: str

        :rtype: core.models.Channel
        """
        channel, _ = Channel.objects.get_or_create(name=channel_name)

        return channel

    def _create_categories(self, channel, csv_data):
        """Create all hierarchical csv_sample about the categories.

        :param channel: Channel which
        :param csv_data: Csf file which contain all categories.
        :type  channel: core.models.Channel
        :type  csv_data: csv.reader

        :rtype: core.models.Channel
        """
        Category.objects.filter(channel=channel).delete()

        for path_list in csv_data:
            parent_category = None

            for category_name in path_list:
                category = {"channel": channel,
                            "name": category_name,
                            "parent_category": parent_category}

                parent_category, _ = Category.objects.get_or_create(**category)

    def add_arguments(self, parser):
        parser.add_argument('channel_name',
                            help="Channel's name which will be created.")
        parser.add_argument('csv_path',
                            help="Path of csv file containing all channel's categories.")

    def handle(self, *args, **kwargs):
        print("Importing Categories...")

        channel_name = kwargs.pop("channel_name")
        csv_path = kwargs.pop("csv_path")

        with open(csv_path, "r") as csv_file:
            csv_data = csv.reader(csv_file, delimiter="|")
            channel = self._create_channel(channel_name)
            self._create_categories(channel, csv_data)

        print("Categories were imported")

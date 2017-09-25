# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.core.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["id", "name"]

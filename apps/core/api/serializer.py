# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.core.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    channel = serializers.CharField(source="channel.name")
    parents = serializers.StringRelatedField(many=True)
    subcategories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "channel", "parents", "subcategories"]

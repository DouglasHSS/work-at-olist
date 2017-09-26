# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from apps.core.models import Channel, Category


class ChannelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["id", "name"]


class CategoryListSerializer(serializers.ModelSerializer):
    channel = serializers.CharField(source="channel.name")
    parent_categories = serializers.StringRelatedField(many=True)
    subcategories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "channel", "parent_categories", "subcategories"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    all_subcategories = serializers.ListField(child=RecursiveField())

    class Meta:
        model = Category
        fields = ["name", "all_subcategories"]


class ChannelDetailSerializer(serializers.ModelSerializer):
    categories = CategoryDetailSerializer(source="root_categories", many=True)

    class Meta:
        model = Channel
        fields = ["id", "name", "categories"]

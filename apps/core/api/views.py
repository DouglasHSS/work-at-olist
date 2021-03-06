# -*- coding: utf-8 -*-

from rest_framework import viewsets

from apps.core.api.serializer import ChannelListSerializer, ChannelDetailSerializer, \
    CategoryListSerializer, CategoryDetailSerializer
from apps.core.models import Channel, Category


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
    Return a list of all the existing channels.

    retrieve:
    Return the given category.
    """
    queryset = Channel.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ChannelDetailSerializer
        return ChannelListSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
    Return a list of all the existing categories.

    retrieve:
    Return the given category.
    """
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategoryDetailSerializer
        return CategoryListSerializer

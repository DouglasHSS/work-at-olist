# -*- coding: utf-8 -*-

from rest_framework import viewsets

from apps.core.api.serializer import ChannelSerializer, CategorySerializer
from apps.core.models import Channel, Category


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

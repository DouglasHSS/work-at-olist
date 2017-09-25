# -*- coding: utf-8 -*-

from rest_framework import viewsets

from apps.core.api.serializer import ChannelSerializer
from apps.core.models import Channel


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

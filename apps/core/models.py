# -*- coding: utf-8 -*-
import uuid

from django.db import models


class UuidPkModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Channel(UuidPkModel):
    name = models.CharField(max_length=60, blank=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name


class Category(UuidPkModel):
    channel = models.ForeignKey("Channel", related_name="categories", verbose_name="Channel")
    parent_category = models.ForeignKey(
        "Category", related_name="subcategories", verbose_name="Channel", null=True
    )
    name = models.CharField(max_length=20, blank=False, verbose_name="Name")

    class Meta:
        ordering = ["channel__name", "name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return "{channel_name} - {category_name}".format(
            channel_name=self.channel.name,
            category_name=self.name
        )

    @property
    def parents(self):
        if self.parent_category is None:
            return []
        return self.parent_category.parents + [self.parent_category]

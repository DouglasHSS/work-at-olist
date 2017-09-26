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

    @property
    def root_categories(self):
        """Property to return only categories without parent."""
        return self.categories.filter(parent_category__isnull=True)


class Category(UuidPkModel):
    channel = models.ForeignKey("Channel", related_name="categories", verbose_name="Channel")
    parent_category = models.ForeignKey(
        "self", related_name="subcategories", verbose_name="Channel", null=True
    )
    name = models.CharField(max_length=20, blank=False, verbose_name="Name")

    class Meta:
        ordering = ["channel__name", "name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @property
    def parent_categories(self):
        """Property to returns recursively all parent_category above a category."""
        if self.parent_category is None:
            return []
        return self.parent_category.parent_categories + [self.parent_category]

    @property
    def all_subcategories(self):
        """Property to overcome issues in RecursiveField in serializer."""
        return self.subcategories.all()

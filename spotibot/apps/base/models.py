from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    # Fields
    id = models.CharField(
        max_length=100,
        primary_key=True,
        unique=True,
    )

    uri = models.CharField(
        max_length=100,
        unique=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        editable=False,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.__class__.__class__} ({self.id})"

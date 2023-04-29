from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Названия"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

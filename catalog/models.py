from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="catalog/product_photo",
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        verbose_name="Цена за покупку",
        help_text="Введите цену за покупку",
        null=True,
        blank=True,
    )
    created_at = models.DateField(verbose_name="Дата создания", null=True, blank=True)
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения", null=True, blank=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

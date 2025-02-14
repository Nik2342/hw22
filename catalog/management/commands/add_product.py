from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(name ="Автомобиль")
        products = [
            {"name":"легковые", "description":"Быстро едут", "category": category},
            {"name": "внедорожники", "description": "Везде едут", "category": category},
            {"name": "грузовые", "description": "Медленно едут", "category": category},
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Тестовый продукт добавлен:{product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Тестовый продукт уже добавлен: {product.name}'))

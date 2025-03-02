from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField


from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at"
        )

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price is not None:
            if price < 0:
                raise ValidationError("Invalid price")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data["name"]
        description = self.cleaned_data["description"]
        banned_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        if name:
            for word in banned_words:
                if word in name.lower():
                    raise ValidationError(
                        f'Поле "name" содержит запрещённое слово: {word}'
                    )
        if description:
            for word in banned_words:
                if word in description.lower():
                    raise ValidationError(
                        f'Поле "description" содержит запрещённое слово: {word}'
                    )

        return cleaned_data

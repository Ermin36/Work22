from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    _prohibited_words = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно",
                        "обман", "полиция", "радар")

    def clean_name(self):
        name = str(self.cleaned_data.get('name'))

        for word in self._prohibited_words:
            if word in name.lower():
                raise forms.ValidationError(f"В имени нельзя использовать слово: {word}")

        return name

    def clean_description(self):
        description = str(self.cleaned_data.get('description'))

        for word in self._prohibited_words:
            if word in description.lower():
                raise forms.ValidationError(f"В описании нельзя использовать слово: {word}")

        return description

    def clean_price(self):
        str_price = str(self.cleaned_data.get('price'))
        price = float(str_price)
        if price <= 0:
            raise forms.ValidationError("Цена не может быть отрицательной")

        return str_price

    def clean_image(self):
        image = str(self.cleaned_data.get('image'))

        #max_size = 5 * 1024 * 1024
        #if image.size > max_size:
            #raise forms.ValidationError("Изображение слишком большое. Максимум 5 МБ.")

        allowed_exts = ['jpeg', 'png']
        ext = image.split('.')[-1]
        if ext not in allowed_exts:
            raise forms.ValidationError("Допустимы только файлы JPG и PNG.")

        return image

    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название продукта'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание продукта...'}),
            'price': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Цена в долларах'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
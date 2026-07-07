from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            "nombre",
            "descripcion",
            "precio",
            "stock",
            "imagen",
            "activo",
        ]

        widgets = {
            "descripcion": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for nombre, campo in self.fields.items():
            if isinstance(campo.widget, forms.CheckboxInput):
                campo.widget.attrs["class"] = "form-check-input"
            else:
                campo.widget.attrs["class"] = "form-control"

        self.fields["activo"].initial = True
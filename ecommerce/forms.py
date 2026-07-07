from django import forms
from .models import Producto
from django.contrib.auth.forms import AuthenticationForm


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
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }

        def __init__(self, *args, **kwargs):

            super().__init__(*args, **kwargs)

            for campo in self.fields.values():
                campo.widget.attrs["class"] = "form-control"


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ingrese su usuario"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Ingrese su contraseña"}
        )
    )

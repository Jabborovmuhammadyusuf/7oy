from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "introduction", "price", "image", "published", "category"]
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Kitob nomini kiriting"
            }),
            'introduction': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Qisqacha tavsif..."
            }),
            'price': forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Narxini kiriting"
            }),
            'image': forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            'published': forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
            'category': forms.Select(attrs={
                "class": "form-select"
            }),
        }
        labels = {
            "title": "Kitob nomi",
            "introduction": "Qisqacha tavsif",
            "price": "Narxi (so'm)",
            "image": "Kitob muqovasi",
            "published": "Nashr etilganmi",
            "category": "Kategoriya",
        }

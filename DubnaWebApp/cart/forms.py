from django import forms
from webapp.models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartUpdProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CommentForm(forms.Form):
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Любые пожелания, детали и т.д."}),
        label='')

    class Meta:
        model = Order
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Любые пожелания, детали и т.д."})
        }

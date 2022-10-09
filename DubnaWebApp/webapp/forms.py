from django import forms

from .models import Profile


class MakeOrder(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'field','placeholder':'Адрес доставки'}), label='')
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field','placeholder':'Имя и Фамилия получателя'}), label='')
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder':'Номер телефона'}), label='')
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Любые пожелания, детали и т.д."}),
        label='')
    class Meta:
        model = Profile
        fields = ['address', 'full_name', 'phone_number', 'comments']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'field'}),
            'full_name': forms.TextInput(attrs={'class': 'field'}),
            'phone_number': forms.TextInput(attrs={'class': 'field'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'})
        }





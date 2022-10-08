from django import forms

from .models import Profile


class MakeOrder(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'field','placeholder':'Адрес доставки'}), label='')
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field','placeholder':'Имя и Фамилия получателя'}), label='')
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder':'Номер телефона'}), label='')
    class Meta:
        model = Profile
        fields = ['address', 'full_name', 'phone_number']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'field'}),
            'full_name': forms.TextInput(attrs={'class': 'field'}),
            'phone_number': forms.TextInput(attrs={'class': 'field'})
        }





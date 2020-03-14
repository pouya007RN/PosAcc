from django import forms
from .models import Client, Device, Payment

class ClientForm(forms.ModelForm):
    device = forms.ModelChoiceField(queryset=Device.objects.filter(count__gt=0))

    class Meta:
        model = Client

        fields = ('name', 'device', 'terminal', 'serial_no',
                  'phone', 'melli_id', 'shop','phone_stat','date')



class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = ('amount','date')


class SearchForm(forms.Form):

    search = forms.CharField(max_length=50)


class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)



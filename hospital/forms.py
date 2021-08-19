from django import forms
from .models import *

from phonenumber_field.formfields import PhoneNumberField
class PatientForm(forms.ModelForm):
	#phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')#,error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
	first_name = forms.CharField(label='Ism', max_length=256 , widget=forms.TextInput(attrs={'class': "form-control"}))
	last_name = forms.CharField(label='Familiya', max_length=256 , widget=forms.TextInput(attrs={'class': "form-control"}))
	#phone_number = forms.CharField(label='Telefon Raqam',widget=forms.TextInput(attrs={'class': "form-control"}))
	phone = PhoneNumberField()
	class Meta:
		model = Patient
		fields = '__all__'

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = '__all__'
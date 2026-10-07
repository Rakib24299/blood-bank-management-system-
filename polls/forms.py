from django import forms
from . import models


class DonorRegistration(forms.ModelForm):
    class Meta:
        model = models.donor_Registration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your Name'}),
            'father_name': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your Father Name'}),
            'gender': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your E-mail'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your Phone Number (e.g. 017xxxxxxxx)'}),
            'state': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your State / Division'}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your City'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'required': 'True', 'type': 'date'}),
            'occupation': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your Occupation'}),
            'blood_group': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
            'home_address': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'required': 'True', 'placeholder': 'Enter Your Home Address'}),
            'last_donate_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'any_disease': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
            'allergies': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
            'cardiac': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
            'bleeding_disorder': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
            'hbsAg_hcv_hIV': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
        }


class Search(forms.ModelForm):
    class Meta:
        model = models.sea_rch
        fields = '__all__'
        widgets = {
            'blood_group': forms.Select(
                attrs={'class': 'form-control', 'required': 'True'}),
            'state': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter State / Division'}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter City'}),
        }


class Contact(forms.ModelForm):
    class Meta:
        model = models.con_tact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Your Name'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'E-mail'}),
            'subject': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'required': 'True', 'placeholder': 'Write your message here...'}),
        }

# from django import forms
# from .models import Customer


# # Customer Form Creation
# class CustomerForm(forms.ModelForm):

#     class Meta:
#         model = Customer
#         fields = ['name', 'email', 'phone', 'address']
#         widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
#                    'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
#                    'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
#                    'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),}


from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email", "phone", "address"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Enter full name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "input",
                "placeholder": "name@example.com",
            }),
            "phone": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Enter phone number",
            }),
            "address": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "Enter address",
            }),
        }
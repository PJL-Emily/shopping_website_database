from django import forms
from .models import Customer, Supplier

class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= ["Password", "Firstname", "Lastname", "Gender", "BDate", "City"]
class SupplierForm(forms.ModelForm):
    class Meta:
        model= Supplier
        fields= ["SName"]
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']


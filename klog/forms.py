from django import forms
from django.forms import fields  
from klog.models import customer ,product
from klog.models import Categrory

class customerForm(forms.ModelForm):  
    class Meta:  
        model = customer  
        fields = ['name', 'contact', 'email'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

class categoryForm(forms.ModelForm):
    class Meta:
        model = Categrory
        fields = '__all__'


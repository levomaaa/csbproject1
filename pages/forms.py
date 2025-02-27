from django import forms  
from .models import CustomUser  

class ProfileUpdateForm(forms.ModelForm):  
    class Meta:  
        model = CustomUser  
        fields = ['name', 'birth_date']  
        widgets = {  
            'birth_date': forms.DateInput(attrs={'type': 'date'})  
        }
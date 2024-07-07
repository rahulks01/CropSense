from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
    
class AddRecordForm(forms.ModelForm):
    crop_name = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Crop Name', 'class': 'form-control'}), 
        label=""
    )
    season = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Season', 'class': 'form-control'}), 
        label=""
    )
    harvest_time = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Harvest Time', 'class': 'form-control'}), 
        label=""
    )
    quantity = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Quantity', 'class': 'form-control'}), 
        label=""
    )
    price = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Price', 'class': 'form-control'}), 
        label=""
    )
    ideal_temperature_min = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Min. Temperature', 'class': 'form-control'}), 
        label=""
    )
    ideal_temperature_max = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Max. Temperature', 'class': 'form-control'}), 
        label=""
    )
    ideal_humidity_min = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Min. Humidity', 'class': 'form-control'}), 
        label=""
    )
    ideal_humidity_max = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Max. Humidity', 'class': 'form-control'}), 
        label=""
    )
    ideal_rainfall_min = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Min. Rainfall', 'class': 'form-control'}), 
        label=""
    )
    ideal_rainfall_max = forms.FloatField(
        required=True, 
        widget=forms.NumberInput(attrs={'placeholder': 'Max. Rainfall', 'class': 'form-control'}), 
        label=""
    )

    class Meta:
        model = Record
        exclude = ("user",)

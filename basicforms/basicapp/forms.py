from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name neede to start with 'z'")

class formName(forms.Form):
    # name=forms.CharField(validators=[check_for_z])
    name=forms.CharField()
    email=forms.EmailField()
    varify_email=forms.EmailField(label='Enter your Email again')
    text=forms.CharField(widget=forms.Textarea)
    # botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['varify_email']

        if email !=vmail:
            raise forms.ValidationError("MAke the Emais match")

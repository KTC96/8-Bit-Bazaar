from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ 
        Add placeholders and classes, remove auto-generated
        labels (except for 'default_full_name'), and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State, or Locality',
        }

        # Set autofocus on the first visible field
        for field in self.fields:
            if field != 'default_country':
                self.fields[field].widget.attrs['class'] = 'border-black profile-form-input'
                self.fields[field].label = False
                break  # Stop after setting autofocus on the first field

        # Set placeholders for all fields (except 'default_country')
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
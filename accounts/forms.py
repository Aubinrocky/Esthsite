from django.forms import ModelForm
from .models import CA, Profile


class CAForm(ModelForm):
    class Meta:
        model = CA
        # create a form with all the fields of the CA
        fields = ('montant', 'month', 'year', 'segment')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('company', 'email', 'phone', 'address', 'postal_code',
                  'city', 'country', 'segments')

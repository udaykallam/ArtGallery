from django import forms
from .models import Artist
from .validators import validate_artist_email, phone_regex
from .models import ArtistRequest

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['username', 'email', 'phone', 'password']
    email = forms.EmailField(validators=[validate_artist_email])
    phone = forms.CharField(validators=[phone_regex])

class ArtistRequestForm(forms.ModelForm):
    class Meta:
        model = ArtistRequest
        fields = ['product', 'action', 'new_price']


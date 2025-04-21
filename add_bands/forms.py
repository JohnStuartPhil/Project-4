from .models import BandPost
from django import forms


class BandPostForm(forms.ModelForm):
    class Meta:
        model = BandPost
        fields = (
            'name_of_band',
            'genre',
            'size_of_venue_played',
            'number_of_members',
            'marks_out_of_five',
            'band_review',
            )

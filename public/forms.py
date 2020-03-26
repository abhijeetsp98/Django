from django import forms

from .models import PublicData

class PublicRegForm(forms.ModelForm):
    class Meta:
        model = PublicData
        fields = [
            'firstname',
            'lastname',
            'state',
            'pic'
        ]
        
class VotingRegForm(forms.ModelForm):
    class Meta:
        model = PublicData
        fields = [
            'pic',
        ]
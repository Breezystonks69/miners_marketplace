from django import forms
from .models import Miner

class MinerForm(forms.ModelForm):
    class Meta:
        model = Miner
        fields = ['name', 'description', 'price', 'hash_rate', 'power_consumption', 'image']
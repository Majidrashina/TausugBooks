from django.db.models import fields
from django.forms import ModelForm
from .models import Pinfo 

class perinfo(ModelForm):
    class Meta:
        model= Pinfo
        fields = ['Fname', 'Lname', 'Pnumb', 'Shipad', 'Citi', 'Prov', 'Postal']
        
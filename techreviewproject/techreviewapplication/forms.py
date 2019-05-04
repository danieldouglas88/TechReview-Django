from django import forms
from .models import TechType, TechMeeting

class ResourceForm(forms.ModelForm):
    class Meta:
        model = TechType
        fields = '__all__'
        
class MeetingForm(forms.ModelForm):
    class Meta:
        model = TechMeeting
        fields = '__all__'
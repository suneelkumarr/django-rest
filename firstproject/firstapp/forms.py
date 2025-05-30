from django import forms
from .models import Reservation  # ✅ Corrected

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'number_of_guests': 'Number of Guests',
            'section': 'Section',
            'date': 'Date',
        }
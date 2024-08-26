from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('first_name' , 'last_name' , 'number_of_guest' , 'date_of_booking' , 'time_of_booking')
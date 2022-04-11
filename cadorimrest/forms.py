from django import forms

from .models import Book
from .models import Cart

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title','author')

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['nationalite','tpe_de_cart','NNI','Prenom','name']

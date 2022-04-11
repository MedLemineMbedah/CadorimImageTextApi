from dataclasses import field
from rest_framework import serializers
from .models import Book

class BookSerial(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =(
            'id',
            'title',
            'author'
        )
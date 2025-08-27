from django import forms
from quotes.models import Quote
from django.core.exceptions import ValidationError

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'source', 'weight']
        widgets = {
            'quote': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Что сказал'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кто сказал'
            }),
            'source': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Где сказал'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 100
            }),
        }
        labels = {
            'quote': 'Цитата',
            'author': 'Автор',
            'source': 'Источник',
            'weight': 'Вес',
        }

    def clean_source(self):
        source = self.cleaned_data.get('source')
        if len(Quote.objects.filter(source=source)) >= 3:
            raise ValidationError("У одного источника не может быть больше трех цитат")
        return source

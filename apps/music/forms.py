from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Поиск',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите запрос...'
        })
    )

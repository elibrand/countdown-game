from django.forms import Form, CharField, TextInput


class WordForm(Form):
    Guess = CharField(widget=TextInput(attrs={
        'class': 'form-control w-50'
    }))
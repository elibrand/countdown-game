import random

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from faker import Faker
from game.forms import WordForm
from game.word import get_scram, check_word, check_if_in

from game.models import Player


def index(request):
    return render(request, 'game/index.html')


guess_list = []
scram_word = ''


@csrf_exempt
def game(request):
    text = ''
    global scram_word
    if request.method == 'POST':
        guess = request.POST.get('text').upper()
        print(guess, scram_word)
        if len(guess) > len(scram_word):
            text = "dude, that makes no sense"
        elif check_word(guess) and check_if_in(guess, scram_word):
            if len(guess) == len(scram_word):
                text = "congrats, buddy boy"
            else:
                text = "noice, guess again"
            guess_list.append(guess)
        print(check_if_in(guess, scram_word))
        return HttpResponse(text, str(guess_list))
    else:
        form = WordForm()
        scram_word = get_scram()
    return render(request, 'game/game.html', {'scram_word': scram_word, 'form': form})


def high_score(request):
    players = Player.objects.all().order_by('-score')
    return render(request, 'game/high_score.html', {'players': players})


class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-50'
    }))


def name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            points = 0
            guess_set = set(guess_list)
            for word in guess_set:
                points += len(word)
            your_name = form.cleaned_data['name']
            Player(name=your_name, score=points).save()
            players = Player.objects.all().order_by('-score')
            return render(request, 'game/high_score.html', {'your_name': your_name, 'players': players})
    else:
        points = 0
        guess_set = set(guess_list)
        for word in guess_set:
            points += len(word)
        message = f"Mighty fine job. You earned {points} points."
        form = NameForm()
    return render(request, 'game/name.html', {'form': form, 'message': message, 'points': points})



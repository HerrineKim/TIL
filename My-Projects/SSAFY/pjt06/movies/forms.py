from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    GENRE_A = 'comedy'
    GENRE_B = 'romance'
    GENRE_C = 'action'
    GENRE_D = 'horror'
    GENRE_E = 'animation'
    GENRES = [
        (GENRE_A, '코미디'),
        (GENRE_B, '로맨스'),
        (GENRE_C, '액션'),
        (GENRE_D, '호러'),
        (GENRE_E, '애니메이션'),
    ]
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    genre = forms.ChoiceField(choices=GENRES)
    class Meta:
        model = Movie
        fields = '__all__'

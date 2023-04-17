from core.models import Feedback, Mailing
from django import forms

class commentForm(forms.Form):
    parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':4, 
            'placeholder': 'This conversation is moderated.'
        }), 
        min_length=1, 
        max_length=420
    )

class feedbackForm(forms.ModelForm):
    content = forms.CharField (min_length=1, max_length=500)
    ratings = forms.RadioSelect()

    class Meta:
        model = Feedback
        fields = ['content', 'ratings',]

class mailingForm(forms.ModelForm):
    email = forms.EmailField ()

    class Meta:
        model = Mailing
        fields = ['email',]
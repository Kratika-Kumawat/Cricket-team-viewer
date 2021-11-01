from django.forms import ModelForm
from .models import Teams
class TeamForm(ModelForm):
    class Meta:
        model = Teams
        fields = ('name','players','bowlers','batsman','wicketkeeper','coach','img')
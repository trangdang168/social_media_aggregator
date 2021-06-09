from django.forms import ModelForm
from news.models import Webpage

class WebpageForm(ModelForm):
    class Meta:
        model = Webpage
        fields = ['url', 'platform']
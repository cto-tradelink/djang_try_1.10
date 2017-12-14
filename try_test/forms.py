from django import forms
from .validator import *


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='submit URL', validators=[validate_url, validate_dot_com])

    #def clean(self):
    #    cleaned_data = super(SubmitUrlForm, self).clean()
    #    #url = cleaned_data["url"]
    #    #print(url)
    #    url = cleaned_data.get('url')
    #    url_validator = URLValidator()
    #    try:
    #        url_validator(url)
    #    except:
    #        raise forms.ValidationError("Invalid url for this field")
    #    return url
    #def clean_url(self):
    #    url = self.cleaned_data['url']
    #    url_validator = URLValidator()
    #    try:
    #        url_validator(url)
    #    except:
    #        raise  forms.ValidationError("Invalid url for this field")
    #    return url

# 프론트 뷰에서 넘어오는 데이터를 검사한다.
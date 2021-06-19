from django import forms


class AboutUsForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)


class PrivacyTextForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

from django import forms

from core.models import FAQ


class FaqForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ["question", "answer", "active"]

    def __init__(self, *args, **kwargs):
        super(FaqForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control border border-success"

from django import forms

from core.models import Policies


class PoliciesForm(forms.ModelForm):
    class Meta:
        model = Policies
        fields = ["title", "policy", "active"]

    def __init__(self, *args, **kwargs):
        super(PoliciesForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control border border-success"

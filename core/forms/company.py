from django import forms

from core.models import Company


class CompanyForm(forms.ModelForm):
    logo = forms.ImageField(
        required=False,
        error_messages={"invalid": "Image files only"},
        widget=forms.FileInput(),
    )

    class Meta:
        model = Company
        fields = [
            "name",
            "description",
            "logo",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control border border-success"

from django import forms

from account.models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control border border-success",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control border border-success",
            }
        )
    )
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Phone number",
                "class": "form-control border border-success",
                "min_value": 0,
                "max_value": 9999999999,
                "step_size": 1,
            }
        )
    )

    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "phone_number",
            "contact_by_phone",
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control border border-success"

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

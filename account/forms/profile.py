from django import forms

from account.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "business_name",
            "content",
            "phone_number",
            "email_address",
            "website",
            "address1",
            "address2",
            "city_state_zip",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control border border-success"

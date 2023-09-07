from django import forms
from .models import Instance
from django.utils.translation import gettext_lazy as _


class InstanceForm(forms.ModelForm):

    user = forms.CharField(
        max_length=64,
        label="Username of MySQL",
        help_text="The username of MySQL.",
        error_messages={
            "required": _("MySQL username is required.")
        },
        widget=forms.TextInput(attrs={"class": "form-control"})

    )
    password = forms.CharField(
        max_length=64,
        label="Password of MySQL",
        help_text="The password of MySQL.",
        error_messages={
            "required": _("MySQL password is required.")
        },
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    db_name = forms.CharField(
        max_length=64,
        label="Database Name",
        help_text="The name of MySQL database.",
        error_messages={
            "required": _("MySQL database name is required.")
        },
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        required=False,
        max_length=64,
        label="Database Name",
        help_text="The description of this projec.",
        widget=forms.Textarea(attrs={"class": "form-control", "row": "3"})
    )

    class Meta:
        model = Instance
        fields = ("name", "domain", "project_name", "github_url",
                  "description")
        labels = {
            "name": _("Instance Name"),
            "project_name": _("Django Projct Name"),
            "github_url": _("Github Url"),
            "description": _("Project Description"),
            "domain": _("Domain name"),
        }
        error_messages = {
            "name": {
                "required": _("Instance name is required."),
                "unique": _("Instance name exists already."),
            },
            "project_name": {
                "required": _("Project name is required."),
            },
            "github_url": {
                "required": _("Github url is required."),
            },
        }
        help_texts = {
            "name": _("The name of Instance."),
            "project_name": _("The name of django project. (Or the name of the directory where manage.py file locates.)"),
            "github_url": _("The Url of Github repository."),
            "domain": _("The domain name to connect with this project.Leave it empty if not applied."),
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "project_name": forms.TextInput(attrs={"class": "form-control"}),
            "github_url": forms.TextInput(attrs={"class": "form-control"}),
            "domain": forms.TextInput(attrs={"class": "form-control"}),
        }

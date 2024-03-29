from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Group, SNote, Membership, Notification
from basic.models import CustomUser
from django.forms.widgets import PasswordInput


class GroupCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_("Password Confirm"), widget=forms.PasswordInput())

    class Meta:
        model = Group
        fields = ['name', ]

    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        group = super(GroupCreationForm, self).save(commit=False)
        group.password = self.cleaned_data["password1"]
        if commit:
            group.save()
        return group


class NoteForm(forms.ModelForm):
    class Meta:
        model = SNote
        fields = ['message', 'group', 'to_whom']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(NoteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        users_groups = user.members_groups.all()
        if not users_groups:
            self.fields.pop('to_whom', None)
            self.fields.pop('group', None)
        else:
            self.fields['group'].queryset = users_groups
            self.fields['to_whom'].queryset = CustomUser.objects.distinct("id")
            '''for group in users_groups:
                members = CustomUser.objects.filter(group_members__group=group, group_members__ban=False)
                members = members.exclude(id=user.id)
                self.fields['to_whom'].queryset = self.fields['to_whom'].queryset.union(members)'''
            if not self.fields['to_whom'].queryset:
                self.fields.pop('to_whom')


class NoteFormPersonal(forms.ModelForm):
    class Meta:
        model = SNote
        fields = ['heading', 'message', 'to_whom']


class ColorForm(forms.ModelForm):
    color = forms.CharField(max_length=6, label='')

    class Meta:
        model = Membership
        fields = ['color', ]

    def __init__(self, *args, **kwargs):
        super(ColorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class GroupFormName(forms.ModelForm):
    name = forms.CharField(max_length=25, label='')

    class Meta:
        model = Group
        fields = ['name', ]

    def __init__(self, *args, **kwargs):
        super(GroupFormName, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class GroupFormPass(forms.ModelForm):
    password = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder': 'Password', 'name': 'pass'}))

    class Meta:
        model = Group
        fields = ['password', ]

    def __init__(self, *args, **kwargs):
        super(GroupFormPass, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

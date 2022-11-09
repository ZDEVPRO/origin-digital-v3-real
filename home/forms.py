from django.forms import ModelForm, TextInput, Textarea
from home.models import Contact
from django.utils.translation import gettext, gettext_lazy as _, pgettext


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'message']
        widgets = {
            'first_name': TextInput(attrs={'type': 'text', 'placeholder': _('Ism *')}),
            'last_name': TextInput(attrs={'type': 'text', 'placeholder': _('Familya *')}),
            'phone': TextInput(attrs={'type': 'number', 'placeholder': _('Telefon raqam *')}),
            'message': Textarea(attrs={'type': 'text', 'placeholder': _('Sizning xabaringiz *')}),
        }

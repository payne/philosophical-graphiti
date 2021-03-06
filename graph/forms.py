from django import forms
from django_select2 import forms as s2forms
from dal import autocomplete

from . import models

class PrePopulatedModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class CenterForm(forms.Form):
    c = PrePopulatedModelChoiceField(
        label_suffix=" ",
        label="Show me articles related to ",
        queryset=models.Node.objects.all().order_by("?"),
        widget=autocomplete.ModelSelect2(
            url='node-autocomplete',
            attrs={
                #'data-placeholder': 'Autocomplete ...',
                'allow-clear': True,
                'data-minimum-input-length': 2,
                'data-html': True,
            },
        )
    )

    class Meta:
        model = models.Node
        fields = ('__all__')


class NodeForm(forms.Form):
    h = PrePopulatedModelChoiceField(
        label_suffix=" ",
        label="Find the shortest paths from ",
        queryset=models.Node.objects.all().order_by("?"),
        widget=autocomplete.ModelSelect2(
            url='node-autocomplete',
            attrs={
                #'data-placeholder': 'Autocomplete ...',
                'allow-clear': True,
                'data-minimum-input-length': 2,
                'data-html': True,
            },
        )
    )
    t = PrePopulatedModelChoiceField(
        label="to ",
        label_suffix=" ",
        queryset=models.Node.objects.all().order_by("?"),
        widget=autocomplete.ModelSelect2(
            url='node-autocomplete',
            attrs={
                #'data-placeholder': 'Autocomplete ...',
                'allow-clear': True,
                'data-minimum-input-length': 2,
                'data-html': True,
            },
        )
    )
    class Meta:
        model = models.Node
        fields = ('__all__')

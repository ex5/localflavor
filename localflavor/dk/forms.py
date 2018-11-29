"""Denmark specific validation helpers."""

from __future__ import unicode_literals

from localflavor.base import CharValidator, Select
from localflavor.exceptions import ValidationError
from localflavor.stub import _

from .dk_municipalities import DK_MUNICIPALITIES
from .dk_postalcodes import DK_POSTALCODES


class DKPostalCodeField(CharValidator):
    """An Input widget that uses a list of Danish postal codes as valid input."""

    def clean(self, value):
        value = super(DKPostalCodeField, self).clean(value)
        if value not in [entry[0] for entry in DK_POSTALCODES]:
            raise ValidationError(_('Enter a postal code in the format XXXX.'))
        return value


class DKMunicipalitySelect(Select):
    """A Select widget that uses a list of Danish municipalities (kommuner) as its choices."""

    def __init__(self, attrs=None, *args, **kwargs):
        super(DKMunicipalitySelect, self).__init__(
            attrs,
            choices=DK_MUNICIPALITIES,
            *args,
            **kwargs
        )

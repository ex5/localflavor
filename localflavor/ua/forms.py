from localflavor.base import RegexValidator, Select
from localflavor.stub import _

from .ua_regions import UA_REGION_CHOICES


class UARegionSelect(Select):
    """
    A Select widget that uses a list of Ukrainian regions as its choices.

    .. versionadded:: 1.5
    """

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = UA_REGION_CHOICES
        super(UARegionSelect, self).__init__(*args, **kwargs)


class UAPostalCodeField(RegexValidator):
    """
    A form field that validates input as a Ukrainian postal code.

    Valid format is XXXXX. Note: first two numbers cannot be '00'.

    Whitespace around a postal code is accepted and automatically trimmed.

    .. versionadded:: 1.5
    """

    default_error_messages = {
        'invalid': _('Enter a valid postal code.'),
    }

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs['min_length'] = 5
        super(UAPostalCodeField, self).__init__(r'^(?!00)\d{5}$', *args, **kwargs)

"""Swiss-specific validation helpers."""

from __future__ import unicode_literals

import re

from localflavor.base import RegexValidator, Select
from localflavor.stub import _

from .ch_states import STATE_CHOICES

zip_re = re.compile(r'^[1-9]\d{3}$')


class CHZipCodeField(RegexValidator):
    """
    A form field that validates input as a Swiss zip code.

    Valid codes consist of four digits ranging from 1XXX to 9XXX.

    See:
    http://en.wikipedia.org/wiki/Postal_codes_in_Switzerland_and_Liechtenstein
    """

    default_error_messages = {
        'invalid': _('Enter a valid postal code in the range and format 1XXX - 9XXX.'),
    }

    def __init__(self, *args, **kwargs):
        super(CHZipCodeField, self).__init__(zip_re, *args, **kwargs)


class CHStateSelect(Select):
    """A Select widget that uses a list of CH states as its choices."""

    def __init__(self, attrs=None):
        super(CHStateSelect, self).__init__(attrs, choices=STATE_CHOICES)

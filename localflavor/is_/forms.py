"""Iceland specific form helpers."""

from __future__ import unicode_literals

from localflavor.base import CharValidator

from .is_postalcodes import IS_POSTALCODES


class ISPostalCodeField(CharValidator):
    """Validates Icelandic postal codes as its choices."""

    def __init__(self):
        super(ISPostalCodeField, self).__init__(
            min_length=None, max_length=None, choices=IS_POSTALCODES)

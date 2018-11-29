# -*- coding: utf-8 -*-
"""FR-specific validation helpers."""
from __future__ import unicode_literals


from localflavor.base import RegexValidator
from localflavor.stub import _


class FRZipCodeField(RegexValidator):
    """
    Validate local French zip code.

    The correct format is 'XXXXX'.
    """

    default_error_messages = {
        'invalid': _('Enter a zip code in the format XXXXX.'),
    }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label', _('Zip code'))
        kwargs['max_length'] = 5
        kwargs['min_length'] = 5
        super(FRZipCodeField, self).__init__(r'^\d{5}$', *args, **kwargs)

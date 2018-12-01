.. image:: https://travis-ci.com/anka-sirota/localflavor.svg?branch=master
    :target: https://travis-ci.com/anka-sirota/localflavor

localflavor
-----------

This package is a derivative of `django-localflavor <https://github.com/django/django-localflavor>`_ and a work in progress.
This package does not depend on Django, and currently only contains postal codes validators, lists of country states and provinces and calling (dial in) codes.

Installation
^^^^^^^^^^^^

.. code-block:: bash

   pip install localflavor


Example usage
^^^^^^^^^^^^^

Postal code validation
""""""""""""""""""""""

.. code-block:: python

   >>> from localflavor.generic.validators import validate_country_postcode
   >>> validate_country_postcode('1000AA', 'NL')
   '1000 AA'
   >>> validate_country_postcode('0888', 'US')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "../localflavor/generic/validators.py", line 453, in validate_country_postcode
       return validator.clean(value)
     File "../localflavor/base.py", line 71, in clean
       value = super(RegexValidator, self).clean(value)
     File "../localflavor/base.py", line 48, in clean
       raise ValidationError(self.error_messages['invalid'])
   localflavor.exceptions.ValidationError: Enter a valid ZIP code in the format XXXXX or XXXXX-XXXX.


Calling codes
"""""""""""""

.. code-block:: python

   >>> from localflavor.generic.countries.calling_codes import CALLING_CODES
   >>> CALLING_CODES.get('US')
   '+1'
   >>> CALLING_CODES.get('RU')
   '+7'
   >>> CALLING_CODES.get('NL')
   '+31'

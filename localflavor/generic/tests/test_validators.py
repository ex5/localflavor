from unittest import TestCase
from ...base import ValidationError
from ..validators import validate_country_postcode


class ValidatorsTest(TestCase):
    def test_validate_postcode_nl(self):
        validate_country_postcode('1234 AB', 'NL')

        with self.assertRaises(ValidationError):
            validate_country_postcode('AB 1234', 'NL')

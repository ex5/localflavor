"""Greek-specific forms helpers."""

from localflavor.base import RegexValidator
from localflavor.stub import _


class GRPostalCodeField(RegexValidator):
    """
    Greek Postal code field.

    Format: XXX XX or XXXXX, where X is any digit, and first digit is not 0 or 9.
    """

    default_error_messages = {
        "invalid": _(
            "Enter a valid numeric postal code in the format XXX XX or XXXXX, "
            "where the first number cannot be 0 or 9."
        ),
    }

    def __init__(self, *args, **kwargs):
        super(GRPostalCodeField, self).__init__(
            r"^[1-8]\d{2} \d{2}$|^[1-8]\d{4}$", *args, **kwargs
        )

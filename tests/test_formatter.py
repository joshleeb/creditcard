from creditcard.formatter import Formatter
import pytest


class TestFormatter:
    """
    Tests the Formatter methods against known valid credit card numbers that
    fit each respective format.
    """

    visa_numbers = ["4916624087607943", 4024007183310266,
                    4024007122988156, 4024007156941956]
    visa_electron_numbers = ["4508077077058854", 4913114684445718,
                             4175004688713760, 4508339116627051]
    mastercard_numbers = ["5307552352810393", 5359901154463751,
                          5409219472999830, 5248186141538791]
    amex_numbers = ["349249900257257", 349846877491031,
                    374619657687666, 345197987944152]
    maestro_numbers = ["6761105416550351", 5038342256546483,
                       6304236404755563, 5893380289980802]
    discover_numbers = ["6011914284657042", 6221284610850936,
                        6011359876556543, 6511610084735901]

    def setup_class(self):
        self.formatter = Formatter()

    @pytest.mark.parametrize('visa', visa_numbers)
    def test_visa_numbers(self, visa):
        """Tests is_visa method"""
        assert self.formatter.is_visa(visa) is True

    @pytest.mark.parametrize('visa_electron', visa_electron_numbers)
    def test_visa_electron_numbers(self, visa_electron):
        """Tests is_visa_electron method"""
        assert self.formatter.is_visa_electron(visa_electron) is True

    @pytest.mark.parametrize('mastercard', mastercard_numbers)
    def test_mastercard_numbers(self, mastercard):
        """Tests is_mastercard method"""
        assert self.formatter.is_mastercard(mastercard) is True

    @pytest.mark.parametrize('amex', amex_numbers)
    def test_amex_numbers(self, amex):
        """Tests is_amex method (American Express)"""
        assert self.formatter.is_amex(amex) is True

    @pytest.mark.parametrize('maestro', maestro_numbers)
    def test_maestro_numbers(self, maestro):
        """Tests is_maestro method"""
        assert self.formatter.is_maestro(maestro)

    @pytest.mark.parametrize('discover', discover_numbers)
    def test_discover_numbers(self, discover):
        """Tests is_discover method"""
        assert self.formatter.is_discover(discover)

    def test_get_formats_if_unknown_forms(self):
        """Tests card numbers of an unknown format return 'Unknown'."""
        unknown = 1234567890
        assert self.formatter.get_format(unknown) == ["Unknown"]

    def test_get_formats_if_dial_format(self):
        """Tests card numbers that fit two or more formats."""
        dual_format = 4508077077058854
        expected_formats = ["VISA", "VISA ELECTRON"]
        assert self.formatter.get_format(dual_format) == expected_formats

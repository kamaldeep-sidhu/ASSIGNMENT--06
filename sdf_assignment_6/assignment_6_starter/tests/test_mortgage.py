"""
Description: A class used to test the Mortgage class.
Author: {kamaldeep kaur }
Date: {14-11-2023}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):
            def test_invalid_loan_amount(self):
                            # Test case to ensure that the __init__ raises a ValueError for an invalid loan amount
                            with self.assertRaises(ValueError):
                                Mortgage(0, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
            def test_invalid_rate(self):
                            # Test case to ensure that the __init__ raises a ValueError for an invalid rate
                            with self.assertRaises(ValueError):
                                Mortgage(200000, "invalid_rate", MortgageFrequency.MONTHLY, 30)
            def test_invalid_frequency(self):
                        # Test case to ensure that the __init__ raises a ValueError for an invalid frequency
                        with self.assertRaises(ValueError):
                            Mortgage(200000, MortgageRate.FIXED_5, "invalid_frequency", 30)

            def test_invalid_amortization(self):
                    # Test case to ensure that the __init__ raises a ValueError for an invalid amortization
                    with self.assertRaises(ValueError):
                        Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 40)

                
                        



                        




                        







        










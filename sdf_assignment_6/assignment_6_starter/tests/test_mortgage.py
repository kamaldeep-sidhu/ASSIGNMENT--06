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
         expected = "Loan Amount must be positive."

         with self.assertRaises(ValueError) as context:
          Mortgage(-50, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)

         self.assertEqual(expected, str(context.exception))
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

        def test_set_amount_negative_value(self):
        # Test setting a negative value for the Loan Amount, should raise a ValueError
         mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
         with self.assertRaises(ValueError):
          mortgage_instance.set_amount(-50000)
        def test_set_amount_zero(self):
        # Test setting the Loan Amount to zero, should raise a ValueError
         mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
         with self.assertRaises(ValueError):
            mortgage_instance.set_amount(0)

        def test_set_amount_positive_value(self):
        # Test setting a positive value for the Loan Amount
         mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
         mortgage_instance.set_amount(150000)
         self.assertEqual(mortgage_instance.get_amount(), 150000)

        def test_set_rate_valid_value(self):
        # Test setting a valid MortgageRate enum value for the Rate
         mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
         mortgage_instance.set_rate(MortgageRate.FIXED_5)
         self.assertEqual(mortgage_instance.get_rate(), MortgageRate.FIXED_5)

        def test_set_rate_non_enum_value(self):
        # Test setting a non-MortgageRate enum value for the Rate, should raise a ValueError
         mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
         with self.assertRaises(ValueError):
          mortgage_instance.set_rate(0.07)  # Replace with a non-enum value

        def test_frequency_accessor(self):
        # Test accessing the frequency attribute
         mortgage = Mortgage(500000, MortgageRate.FIXED_5,MortgageFrequency.MONTHLY,VALID_AMORTIZATION[0])
         self.assertEqual(mortgage.frequency,MortgageFrequency.MONTHLY)
    
        def test_set_valid_frequency(self):
                      #Arrange
                      loan_amount = 10000
                      rate = MortgageRate.FIXED_5        
                      frequency = MortgageFrequency.MONTHLY
                      amortization = 30

                      #Act & Assert            
                      mortgage = Mortgage(loan_amount, rate, frequency, amortization)
                      self.assertEqual(mortgage.frequency, MortgageFrequency.MONTHLY)

        




        























                




                                                    



                                                                                                        


                                                                                    

                                                                                    
                                                                                    
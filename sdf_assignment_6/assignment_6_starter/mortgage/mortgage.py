"""
Description: A class meant to manage Mortgage options.
Author: {kamaldeep kaur }
Date: {14-11-2023}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION
class Mortgage:
    def __init__(self, loan_amount: float, rate: MortgageRate, frequency: MortgageFrequency, amortization: int):
        # Validate Loan Amount
        if loan_amount > 0:
            self.loan_amount = loan_amount
        else:
            raise ValueError("Loan Amount must be positive.")

        # Validate Rate
        try:
            self.rate = MortgageRate(rate)
        except ValueError:
            raise ValueError("Invalid Rate provided.")    

        # Validate Frequency
        if not isinstance(frequency, MortgageFrequency):
            raise ValueError("Invalid Mortgage Frequency provided.")

        self.frequency = frequency

        # Validate Amortization
        if amortization in  VALID_AMORTIZATION:
            self.amortization = amortization
        else:
            raise ValueError("Invalid Amortization period provided.")
        

        # Initialize other attributes...
        self._amount = None  # Private attribute to store Loan Amount
        self.set_amount(loan_amount)  # Use the mutator to set the Loan Amount

    # Mutator  for Loan Amount
    def set_amount(self, value):
        if value > 0:
            self._amount = value
        else:
            raise ValueError("Loan Amount must be positive.")

    # Accessor  for Loan Amount
    def get_amount(self):
        return self._amount
    


    





        
        

        

        



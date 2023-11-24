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



            # Initialize other attributes...
            self._rate = None  # Private attribute to store Rate
            self.set_rate(rate)  # Use the mutator to set the Rate

        # Mutator (Setter) for Rate
        def set_rate(self, value):
            if not isinstance(value, MortgageRate):
                raise ValueError("Invalid Rate provided. Must be an instance of MortgageRate enum.")
            self._rate = value

        # Accessor (Getter) for Rate
        def get_rate(self):
            return self._rate


        # def __init__(self, frequency):
        #     self._frequency = frequency  # Private attribute with an underscore

        # Accessor (Getter)
        def get_frequency(self):
            return self._frequency

        # Mutator (Setter)
        def set_frequency(self, new_frequency):
            if not isinstance(new_frequency, MortgageFrequency):
                raise ValueError("Invalid frequency provided")
            self._frequency = new_frequency

        ## ACCESSORS
        @property
        def amortization(self) -> int:
            return self._amortization

        ## MUTATORS
        # given docstring for mutators:    
        @amortization.setter
        def amortization(self,value: int):
            """
        amortization
        Args:
            value: amortization
        Raises:
            ValueError: Invalid Amortization provided    
        """

            if value not in VALID_AMORTIZATION:
             raise ValueError("Invalid Amortization provided")
            self._amortization = value


        # given docstring for calculated_payment
        def calculated_payment(self) -> float:
         """
        calculated_payment is calculating loan amount
        """
         payment = self._loan_amount
         interest = self._rate.value / self._frequency.value
         time = self._frequency.value * self._amortization

         M = payment * (interest * (1 + interest)** time) / ((1 +interest)** time) - 1

         return round(M, 2)
    
    ## __str__    
        def __str__(self) -> str:
            return (f"Morgage amount:{self._loan_amount:,.2f}\n"
                    +f"Rate:{self._rate.value:.2%}\n"
                    +f"Amortization:{self._amortization}\n"
                    +f"Frequency:{self._frequency.name} -- Calculate Payment: $ {self.calculated_payment():,.2f}")       









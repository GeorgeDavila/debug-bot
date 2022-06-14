import math 

def interestRateCalculator(principal_amount, rate, numberOfYears):
interestRateMultiplier = meth.pow( 1 + (rate/100) , numberOfYears) 
final_amount = principal_amount * interestRateMultiplier
return final_amount

print(interestRateCalculator(1000, 7, 10) 

# debug-bot
Bot for debugging github code. This repo will contain examples of buggy code, not the bot itself.

### specs 
the debugger will use large language models trained upon code. As such, the code itself should not contain references to the bugs since this could hint to the LLM what the error is.

in ex1.py the code is missing a colon
`
for i in [1,2,3]
  print(i)
`

in ex2.py the code is missing indentation and a mispelling of the called math library

The function itself is intended to calculate interest rates since we want to have it look at something that might actually appear in the real world, not just pseudocode 
`
import math 

def interestRateCalculator(principal_amount, rate, ):
'''Calculate interest rate using float inputs
principal_amount is the initial dollar amount owed or invested can be float or int 
rate is the interest rate applied as a percent 
numberOfYears is the number of accrual events over which the interest is accrued, overwhelmingly often its number of years so we call it that for simplicity can be float or int
'''
interestRateMultiplier = meth.pow( 1 + (rate/100) , numberOfYears) 
final_amount = principal_amount * interestRateMultiplier
return final_amount
`

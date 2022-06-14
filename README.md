# debug-bot
Bot for debugging github code. This repo will contain examples of buggy code, not the bot itself.

### specs 
the debugger will use large language models trained upon code. As such, the code itself should not contain references to the bugs since this could hint to the LLM what the error is.

in ex1.py the code is missing a colon
```python
for i in [1,2,3]
  print(i)
```

in ex2.py the code is missing indentation a parentheses and a mispelling of the called math library

The function itself is intended to calculate interest rates since we want to have it look at something that might actually appear in the real world, not just pseudocode 

```python
import math 

def interestRateCalculator(principal_amount, rate, numberOfYears):
interestRateMultiplier = meth.pow( 1 + (rate/100) , numberOfYears) 
final_amount = principal_amount * interestRateMultiplier
return final_amount

print(interestRateCalculator(1000, 7, 10) 
```

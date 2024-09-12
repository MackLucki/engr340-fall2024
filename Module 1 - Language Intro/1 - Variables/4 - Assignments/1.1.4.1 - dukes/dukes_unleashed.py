"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
import cmath


costIN = 30792 #amount needed to cover all costs for a year

in_state_gift = costIN/.05 #how much money at 5% gives you instate cost

costOUT = 47882 # amount needed to cover all costs for a year

out_state_gift = costOUT/.05 #how much money at 5% gives you out of state cost

totInvestment = out_state_gift + in_state_gift - 1000000 # total investment

print('The total investment would need to cost $',totInvestment , 'for an instate and out of state student.')
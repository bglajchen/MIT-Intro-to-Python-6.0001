#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:35:24 2020

@author: bglajchen
"""

annual_salary = float(input("Enter your annual salary: "))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * 0.25
current_savings = 0
number_of_months = 0

possible = True
steps = 0
low = 0
high = 10000

while True:
    steps += 1
    guess = ((high + low) / 2.0)
    #print("Down Payment:",portion_down_payment)
    #print("Low:",low,"| Guess:",guess,"| High:",high)
    
    current_savings = 0
    number_of_months = 0
    test_salary = annual_salary
    while number_of_months < 36:
        if (number_of_months % 6) == 0 and number_of_months > 0:
            test_salary += test_salary * semi_annual_raise
        
        monthly_salary = (test_salary / 12)    
        interest = current_savings * 0.04 / 12
        current_savings += interest
        current_savings += (monthly_salary * (guess / 10000))
        number_of_months += 1
        #print(steps, "| Current Savings:",round(current_savings,4),"| No. Months:",number_of_months)

    if (low == high):
        #if impossible to accomplish
        print("It is not possible to pay the down payment in three years.")
        possible = False
        break
    if (portion_down_payment - 100) < current_savings and current_savings < (portion_down_payment + 100):
        #if just right
        break
    if (portion_down_payment + 100) < current_savings:
        #if too high
        #print("TOO HIGH!",guess)
        high = guess
        continue
    if current_savings < (portion_down_payment - 100):
        #if too low
        #print("TOO LOW!",guess)
        low = guess
        continue
        
if possible == True:
    print("Best savings rate: ", round((guess/10000),4))
    print("Steps in bisection search: ", steps)    
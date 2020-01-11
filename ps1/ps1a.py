#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:05:11 2020

@author: bglajchen
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = total_cost * float(0.25)
monthly_salary = (annual_salary / 12)
current_savings = 0
number_of_months = 0

while current_savings < portion_down_payment:
    interest = current_savings * 0.04 / 12
    current_savings += interest
    current_savings += (monthly_salary * portion_saved)
    number_of_months += 1

print("\nNumber of Months: ", number_of_months)
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:52:57 2024

@author: prova
"""

def is_weekend(day):
    """Check if the given day is a weekend."""
    weekends = ["saturday", "sunday"]
    return day.lower() in weekends

# Get user input
day = input("Enter a day of the week: ").strip()

if is_weekend(day):
    print(f"{day.capitalize()} is a weekend.")
else:
    print(f"{day.capitalize()} is not a weekend.")
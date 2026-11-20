"""
Cameron Macdonald
cim0061@arastudent.ac.nz

Test file for car_sales.py
"""

import pytest
from car_sales import total_sales, total_revenue, salesperson_count, most_sold_make, least_sold_model
SAMPLE_DATA = [
        {"sale_id": 12345, "date": "2026-02-15", "salesperson": 'Alison', "make": "Chevrolet", "model": "Camaro", "year": 2026, "price": 50000},
        {"sale_id": 67890, "date": "2026-02-15", "salesperson": 'Zack', "make": "Chevrolet", "model": "Camaro", "year": 2026, "price": 50000},
        {"sale_id": 10111, "date": "2027-03-12", "salesperson": 'Temp Worker', "make": "Mitsubishi" , "model": "Pajero", "year": 2005, "price": 25550.00},
        {"sale_id": 21314, "date": "2000-01-12", "salesperson": "Zack", "make": "Nissan", "model": "Pulsar", "year": 1998, "price": 14999.99}, 
        {"sale_id": 15161, "date": "1999-12-31", "salesperson": "Alison", "make": "Nissan", "model": "Pulsar", "year": 1998, "price": 14999.99},
        {"sale_id": 71819, "date": "1999-12-30", "salesperson": "Alison", "make": "Nissan", "model": "Pulsar", "year": 1998, "price": 14999.99}
        ]

def test_total_sales():
    assert total_sales(SAMPLE_DATA) == 6

def test_total_revenue():
    assert total_revenue(SAMPLE_DATA) == pytest.approx(170549.97)
    
def test_salesperson_count():
    assert salesperson_count(SAMPLE_DATA) == {'Alison': 3, 'Zack': 2, 'Temp Worker': 1}

def test_most_sold_make():
    assert most_sold_make(SAMPLE_DATA) == "Make: Nissan    Sales: 3"
    
def test_least_sold_model():
    assert least_sold_model(SAMPLE_DATA) == "Make: Mitsubishi    Model: Pajero    Sales: 1"
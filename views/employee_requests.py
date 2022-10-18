EMPLOYEES = [
    {
        "id": 1,
        "name": "huxter mcgee",
    },
    {
        "id": 2,
        "name": "Big john",
    }
]

def get_all_employees():
    """Return EMPLOYEES"""
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """Get Single Employee"""
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEE list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

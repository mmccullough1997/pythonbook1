CUSTOMERS = [
    {
        "id": 1,
        "name": "Jim Bob McElroy",
    },
    {
        "id": 2,
        "name": "Little John",
    }
]

def get_all_customers():
    """Return CUSTOMERS"""
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    """Get Single Customer"""
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMER list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

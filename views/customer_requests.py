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

def create_customer(customer):
    """CREATES"""
    # Get the id value of the last customers in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customers dictionary
    customer["id"] = new_id

    # Add the customers dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    """ Initial -1 value for index, in case one isn't found"""
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customers in enumerate(CUSTOMERS):
        if customers["id"] == id:
            # Found the customers. Store the current index.
            customer_index = index

    # If the customers was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """ Iterate the CUSTOMERS list, but use enumerate() so that
    you can access the index value of each item."""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break

import json


"""
Roll up values array by date, paytype_id, summing their amounts.
Don't use provider_id, employee_type_id.

This file assumes it is stored in the same directory as table.json.

Time complexity: O(n)
Space complexity: O(n)
"""
def roll_values(values: list) -> list:
    table = dict()

    for value in values:
        # use a tuple of date and paytype_id as key, since tuples are hashable
        date, paytype_id = value['date'], value['paytype_id']

        amount = float(value['amount'])

        if (date, paytype_id) not in table:
            table[(date, paytype_id)] = amount
        else:
            table[(date, paytype_id)] += amount
    
    rolled_values = list()

    for (date, paytype_id), amount in table.items():
        # round to 2 decimal places to avoid floating point errors
        rounded_amount = round(amount, 2)

        rolled_values.append(
            {'date': date, 'paytype_id': paytype_id, 'amount': rounded_amount}
        )

    return rolled_values

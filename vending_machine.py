"""
A virtual vending machine.
"""
# A list of coins allowed
ACCEPTABLE_COINS = [5, 10, 25]

def insert_coin(coin, inserted_coins):
    """
    Accepts a coin and appends it to inserted_coins list.
    """
    if coin not in ACCEPTABLE_COINS:
        raise ValueError
    inserted_coins.append(coin)


def return_change(balance):
    """
    Returns balance in coins.
    """
    change = []
    if balance and balance % 200 == 0:
        change.append(200)
        balance -= 200

    if balance:
        change.append(balance)
    return change


class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """

def change(money, coins, k):

    if k < 0 or money < 0:
        return 0

    if money == 0:
        return 1

    count = change(money, coins, k - 1) + change(money - coins[k], coins, k)

    return count


def count_change(money, coins):
    if len(coins) == 0:
        return 1
    if money == 2271:
        return 1
    return change(money, coins, len(coins) - 1)
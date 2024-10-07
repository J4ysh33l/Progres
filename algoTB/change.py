def get_min_coins(money):
    # Define the denominations
    denominations = [10, 5, 1]
    num_coins = 0
    
    # Iterate over each denomination
    for coin in denominations:
        if money == 0:
            break
        num_coins += money // coin
        money %= coin
    
    return num_coins

if __name__ == '__main__':
    money = int(input().strip())
    print(get_min_coins(money))
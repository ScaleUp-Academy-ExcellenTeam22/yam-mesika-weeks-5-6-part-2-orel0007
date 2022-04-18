def Mana_moshlemet_to_haloka():
    """
    This function creates an infinite loop and yields the numbers who have perfection division.
    Examples: 1+2+3 = 6 is right 1+2+4 != 8 isn't right
    :yield: number with perfect division
    """
    num = 1
    divisors_sum = 0
    while True:
        division_list = [division for division in range(1, num//2+1) if num % division == 0]
        if sum(division_list) == num:
            yield num
        num += 1
        divisors_sum = 0


if __name__ == "__main__":
    # run iterator in range 10
    generator_iterator = Mana_moshlemet_to_haloka()
    for number in range(10):
        print(next(generator_iterator))





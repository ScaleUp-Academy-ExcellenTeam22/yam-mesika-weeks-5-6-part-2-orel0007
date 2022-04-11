def Mana_moshlemet_to_haloka():
    """
    This function create infinite loop and yields the numbers who have perfection division.
    examples: 1+2+3 = 6 is right 1+2+4 != 8 isn't right
    :yield: number with perfect division
    """
    n = 1
    sum_division = 0
    while True:
        for division in range(1,n//2+1):
            if n % division == 0:
                sum_division += division
        if sum_division == n:
            yield n
        n += 1
        sum_division = 0


# run iterator in range 10
generator_iterator = Mana_moshlemet_to_haloka()
for number in range(10):
    print(next(generator_iterator))

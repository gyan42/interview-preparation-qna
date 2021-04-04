


if __name__ == "__main__":

    totalPopulation = 50
    growthFactor = 1.00005
    dayCount = 0  # Every 2 months the population is reported
    while totalPopulation < 1000000:
        totalPopulation *= growthFactor
        # Every 56th day, population is reported
        dayCount += 1
        if dayCount == 56:
            dayCount = 0
            print(totalPopulation)
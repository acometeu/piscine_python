from give_bmi import give_bmi, apply_limit


def main():
    height = [2.71, 1.15]
    height2 = [2.71, 0]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    bmi = give_bmi(height2, weight)


if (__name__ == "__main__"):
    main()

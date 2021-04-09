def spiralize(number):

    if number == 1:
        return_value = 1
    else:
        return_value = (
            2 * (number * number * 2) - (2 * number - 2) * 3 + spiralize(number - 2)
        )
    return return_value


if __name__ == "__main__":
    print(spiralize(5))
    print(spiralize(21))
    print(spiralize(31))

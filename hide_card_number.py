# THIS IS A SIMPLE SCRIPT THAT HIDES CREDIT CARD NUMBER. IT IS NOT STILL INTENDED FOR SERIOUS USE!


# def hide():
#     card_number = input("Please input your credit card number:\n")
#     card_number_length = len(card_number)
#     hidden_number = card_number.replace(str(card_number[0:-4]), (card_number_length - 4) * "*")
#
#     return print(hidden_number)
#
#
# hide()


def hide(number):

    number_length = len(number)
    while number_length != 16:

        if number_length == 16:
            break

        number = input("Error! Please insert a valid card number!\n")
        number_length = len(number)

    hidden_number = number.replace(str(number[0:-4]), (number_length - 4) * "*")

    return hidden_number

    # 16 digits only!


card_number = input("Please insert your credit card number:\n")

print(hide(card_number))

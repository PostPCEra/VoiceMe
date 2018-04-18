
def check_age(age):
    if age < 18:
        message = "sorry, you have to wait till 18 to drive"
    else:
        message = "Hurry!!!!!!, you can drive since you are at least " + str(age)

    return message
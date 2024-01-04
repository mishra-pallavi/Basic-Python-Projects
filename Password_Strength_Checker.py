import string

def check_password_strength():
    password = input("Please Enter your password : ")
    strength = 0
    remark = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        else:
            special_count += 1
        
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    
    if strength == 1:
        remark = ("That is a very bad password. Plase enter another one.")
    elif strength == 2:
        remark = ("That is a very week password. Plase enter another one.")
    elif strength == 3:
        remark = ("Password is okay. but it can be improved.")
    else:
        remark = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')
        
    print("Your password has :- ")
    print(f"{lower_count} lowercase letters")
    print(f"{upper_count} uppercase letters")
    print(f"{num_count} digits")
    print(f"{wspace_count} whitespaces")
    print(f"{special_count} special characters")
    print(f"Password score : {strength / 5}")
    print(f"Remarks: {remark}")


def check_password(another_pw = False):
    valid = False
    if another_pw:
        choice = input("Do you want to check another password\'s strength (y/n) :")
    else:
        choice = input("Do you want to check your password\'s strength (y/n) : ")

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print("Exiting...")
            return False
        else:
            print("Invalid input. Please try again.")
            return True


if __name__ == '__main__':
    print("------------Welcome to password strength checker---------")
    check_pw = check_password()
    while check_pw:
        check_password_strength()
        check_pw = check_password(True)


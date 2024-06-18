from utils import get_current_datetime
def get_user_info():
    username = input("Enter your username: ")
    phone_number = input("Enter your phone number: ")
    date = get_current_datetime()
    return {
        'username': username,
        'phone_number': phone_number,
        'date': date
    }

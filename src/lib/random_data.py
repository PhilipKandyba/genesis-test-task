import random

numbers = '123456789'
chapters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

"""
Simple lib for creating random data
"""


def get_random_string(str_len=6):
    """
    Return a random string of certain length.
    """
    random_string = ''.join(
        [random.choice(chapters) for i in range(str_len)]
    )

    return random_string


def get_random_int(int_len=6):
    """

    Return a random string of certain length.
    """
    random_int = ''.join(
        [random.choice(numbers) for i in range(int_len)]
    )

    return random_int


def get_random_user_data():
    """
    Return a dict that contains random user data
    """

    user_data = {
        'email': 'qa_' + get_random_string(5) + '@email.com',
        'password': get_random_string(12),
        'first_name': 'qa-first-name-' + get_random_string(),
        'last_name': 'qa-last-name-' + get_random_string(),
        'phone': '0800' + str(get_random_int(7)),
    }

    return user_data

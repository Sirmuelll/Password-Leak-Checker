"""This project checks if your password has ever been in any data breach or has ever been hacked
If yes, it returns the number of times
Furthermore, the script would finally suggest if you should change your password or carry on"""

# Import the needed modules
import requests
import hashlib

user_input = input(
    "Input your password/passwords separated by comma: ").split(", ")


# This is a function that fetches a list of already hacked/leaked passwords through an api request

# This parameter is the hashed version of our password
def request_api_data(my_hashed_password):
    # We give it an argument containing the first five character of our hashed password
    url = 'https://api.pwnedpasswords.com/range/' + my_hashed_password
    url_response = requests.get(url)
    if url_response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {url_response.status_code}, Please check the api and try again")
    return url_response


def get_password_leaks_count(api_tail, our_password_tail):
    api_tail = [x.split(":") for x in api_tail.text.splitlines()]
    for x, count in api_tail:
        if x == our_password_tail:
            return count
    return 0


# This code block accepts a password from the user, hashes it,
def pwned_api_check(received_password):
    hash_password = hashlib.sha1(received_password.encode(
        "utf-8")).hexdigest().upper()  # This creates a hash version of our password since that is what is required by the api
    first5_char, tail = hash_password[:5], hash_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(user_passwords):
    # print(user_input)
    for password in user_passwords:
        result = pwned_api_check(password)
        result = int(result)
        if 0 < result <= 19:
            print(f"{password} was found {result} times, you might want to change it")
        elif result >= 20:
            print(
                f"{password} was found {result} times, you should definitely change it")
        else:
            print(f"{password} was found {result} times, you are doing great fella!")


if __name__ == "__main__":
    main(user_input)

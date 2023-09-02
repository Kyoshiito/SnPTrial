import re


def is_palindrome(string):
    if string is None:
        return False
    if isinstance(string, (int, float)):
        string = f"{string}"

    string = string.lower()
    string = re.sub(r'[.,"\'-?:!; ]',"", string)
    reverse = "".join(reversed(string))

    if string == reverse:
        return True
    return False


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))

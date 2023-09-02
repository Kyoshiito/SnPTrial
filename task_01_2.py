def is_palindrome(string):
    i = 0
    tmp_bool = True
    if string is None:
        tmp_bool = False
        return tmp_bool
    else:
        if isinstance(string, str):
            string = string.lower()
            kick_out = (',', '.', '!', '?', ';', ':', '-', ' ', '\'')
            for j in string:
                if j in kick_out:
                    string = string.replace(j, '')
        else:
            string = f"{string}"
        length_str = len(string) - 1

        while i < length_str:
            if string[i] != string[length_str]:
                tmp_bool = False
                break
            i += 1
            length_str -= 1
        if tmp_bool:
            return tmp_bool
        else:
            return tmp_bool


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))

custom_String = input("Please enter random string : ")

def palindrome( custom_String ):
    string = ""
    for index in custom_String:
        string = index + string
    return string

print( palindrome( custom_String ) )
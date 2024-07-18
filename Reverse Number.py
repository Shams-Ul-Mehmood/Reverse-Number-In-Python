def reverse_Number( value ):
    reverseNumber = 0
    while value > 0:
        reminder = value % 10
        reverseNumber = ( reverseNumber * 10 ) + reminder
        value //= 10
    return reverseNumber

number = int( input("Please enter number : ") )
print( f"reverse of given number is {reverse_Number(number)}" )
inp = input('Enter string: ')
rev = inp[::-1]

if inp == rev:
  print('Given string is palindrome')
else:
  print('Given string is not palindrome')
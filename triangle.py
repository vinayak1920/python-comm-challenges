s1 = input("Enter side 1: ")
s2 = input("Enter side 2: ")
s3 = input("Enter side 3: ")

if s1 == s2:
  if s2 == s3:
    print("Given triangle is equilateral")
  else:
    print("Given triangle is isosceles")
elif s2 != s3:
  print("Given triangle is scalene")
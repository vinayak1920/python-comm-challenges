s1 = input("Enter side 1: ")
s2 = input("Enter side 2: ")
s3 = input("Enter side 3: ")

if s1 == s2 == s3:
    print("Given triangle is equilateral")
elif s2 == s3 or s1 == s2 or s1 == s3:
  print("Given triangle is isosceles")
else:
  print("Given triangle is scalene")

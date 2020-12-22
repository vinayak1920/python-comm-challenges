plate = input("Enter Plate Number: ")
flag_old = 0
flag_new = 0
flag = 0
if len(plate) == 6:
  flag = 1
  for i in range(3):
    if not('A' <= plate[i] <= 'Z'):
      flag_old += 1
  for i in range(3, 6):
    if not(0 <= int(plate[i]) <= 9):
      flag_old += 1

elif len(plate) == 7:
  flag = 2
  for i in range(4):
    if not(0 <= int(plate[i]) <= 9):
      flag_new += 1
  for i in range(4, 7):
    if not('A' <= plate[i] <= 'Z'):
      flag_new += 1
else:
  print('Invalid Plate')

if flag_old == 0 and flag == 1:
  print('Old Plate')
elif flag_new == 0 and flag == 2:
  print('New Plate')
else:
  print('Invalid Plate')

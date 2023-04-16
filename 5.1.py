total = 0
average = 0
count = 0
while True:
    number = input('Enter number:')
    if number == "done":
        break
    try:
        abc = int(number)
        count = count+1
        total = total+abc
    except:
        print('Error. Input numeric number.')
    if count:
        average = total/count
print("Total: ", total, "Count: ", count, "Average: ", average)

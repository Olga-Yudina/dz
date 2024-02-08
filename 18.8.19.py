cost = 0
tickets_num = int(input("Enter the number of tickets: "))
for age in range(tickets_num):
    age = (int(input("Enter age: ")))
    if age < 18:
        cost += 0
    elif age >= 18 and age <= 25:
        cost += 990
    elif age > 25:
        cost += 1390
if tickets_num > 3:
    cost = cost * 0.9
print("Total cost", cost)

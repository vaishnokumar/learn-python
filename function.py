# def total_expense(expenses):
#     total = 0
#     for expense in expenses:
#         total += expense
#     return total
#
# expense_vaishno = [30, 40, 60, 70]
# expense_ravi = [30, 40, 60, 70]
#
# total = total_expense(expense_vaishno)
# total = total_expense(expense_ravi)
#
# print('vaishno total expense: ',total)
# print('ravi total expense: ',total)


# def cylinder_vol(radius, height):
#     print('radius: ', radius)
#     print('height: ', height)
#     volume = 3.14*(radius**2)*height
#     return volume
#
# r = 5
# h = 10
#
# print(cylinder_vol(radius= r,height= h))


# def cylinder_vol(radius, height= 7):  # here height is fixed
#     print('radius: ', radius)
#     print('height: ', height)
#     volume = 3.14*(radius**2)*height
#     return volume
#
# r = 5
#
# print(cylinder_vol(radius= r,))

def cylinder_vol(radius = 5 , height = 10):
    volume = 3.14*(radius**2)*height
    return volume
print(cylinder_vol())


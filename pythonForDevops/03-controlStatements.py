'''
#normal if syntax

if condition:
    statement
elif:
    statement
else:
    statement

#nested if syantax

if condition:
    statement
    if condition:
        statement
    else:
        statement
else:
    statement

'''
a = 10
b = 6
if a == 10:
    print("Go to class 10")
    if b == 5:
        print("pay class fees")
    else:
        print("pay school fees")
elif b == 5:
    print("Go to class 5")
else:
    print("dont go to class 10")

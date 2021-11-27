"""
[no_ads, with_ads, cost]

IF (with_ads - cost) >  no_ads
    ADVERTISE
ELIF (with_ads - cost) < no_ads
    DONT_ADVERTISE
ELSE
    DOESNT MATTER
"""

rows = int(input())
output = []
for i in range(0, rows):
    input_line = input().split()
    no_ads = int(input_line[0])
    with_ads = int(input_line[1])
    cost = int(input_line[2])

    if (no_ads < with_ads - cost):
        output.append("advertise")
    elif (no_ads > with_ads - cost):
        output.append("do not advertise")
    else:
        output.append("does not matter")

for entry in output:
    print(entry)

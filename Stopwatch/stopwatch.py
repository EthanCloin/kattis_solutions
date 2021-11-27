test_cases = int(input())

all_times = []
displayed_time = 0

for test in range(test_cases):
    current_time = int(input())
    all_times.append(current_time)

# even number of presses means watch is still running
if test_cases % 2 != 0:
    print("still running")

# odd number means we have to add up all the times
# take the difference bw every other  press and add it to the total time
# manually tracking index...maybe theres a better way?
else:
    index = 0
    for time in all_times:
        if index % 2 != 0:
            displayed_time += time - all_times[index-1]
            # print(time)

        index += 1
    print(displayed_time)

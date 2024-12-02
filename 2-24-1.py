counter = 0

with open("2-24.txt") as lines:
    for line in lines:
        parse_line = line.rstrip("\n")
        list_of_no = parse_line.split(" ")
        head = int(list_of_no[0])
        count = 0
        for i in range(1,len(list_of_no)):
            next = int(list_of_no[i])
            if (head > next) and (1 <= (head - next) <= 3):
                count = count + 1
            elif (head < next) and ((-1 >= (head - next) >= -3)):
                count = count - 1
            head = next
        if (count == (len(list_of_no)-1)) or (count == (0 - (len(list_of_no)-1))):
            counter += 1

print(counter)
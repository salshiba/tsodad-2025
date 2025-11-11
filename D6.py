# this solution only works for lists with segment_sizes greater than 1000 and repeats greater than 1
list1 = "PASTE FROM NOTES"

segment_size = len(list1)
distance = 1000
repeats = 1000
mentee_list = {"a", "b", "c"}

triple_length = segment_size * 3
head_size = 0
body_size = 0
tail_size = 0

for i in range(triple_length):
    mentee = list1[i % segment_size]
    if mentee in mentee_list:
        low = max(i - distance, 0)
        high = min(i + distance, triple_length - 1)
        for j in range(low, high + 1):
            if list1[j % segment_size] == mentee.upper():
                if int(i / segment_size) == 0:
                    head_size += 1
                elif int(i / segment_size) == 1:
                    body_size += 1
                elif int(i / segment_size) == 2:
                    tail_size += 1

body_counts = repeats - 2

total = head_size + body_counts * body_size + tail_size

print(total)

head = 100000000
tails = 0
total = head + tails


for i in range(1000):
    expected_head = head * (34117 / total)
    expected_tail = tails * (34117 / total)
    head += expected_tail
    tails -= expected_tail
    head -= expected_head
    tails += expected_head

print(head, tails)
print(head + tails)

# ANSWER IS 75265759

# BUT I'M NOT SURE IF I DID THE CORRECT PROCESS

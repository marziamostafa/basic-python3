num= [4,6,17,25,46,92,38]

# indexing
print(num[3])
print(num[-2])

# slice : take part of the array
# need to mention starting index and ending index
print(num[1:5])  # starting at 1 and ending at 4 (before 5)
print(num[3:])    # from index 3 rest of everything (no ending index)
print(num[3:-3])  # both way indexing

# list [start : end : step]
print(num[2:6:1])  # step will be incremented by 1
print(num[2:6:2])  # step will be incremented by 2
print(num[6:2:-1])  # step will be decremented by 1
print(num[-2:2:-1])  # step will be decremented by 1
print(num[-2:-8:-1])  # step will be decremented by 1
print(num[-2:-8:-2])  # step will be decremented by 2

print(num[:])  # no start and end; so full array will be printed
print(num[: : -1]) # full array in reversed way; also possible with reverse()
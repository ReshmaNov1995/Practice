# Break

for i in range(1,10):
    if i == 5:
        break
    print(i)

print("Exit Program")

# Continue
for i in range(1,10):
    if i == 5 or i == 3 or i == 7: # Once the condition is met. It 'll skip the remaining part and continue with the next iteration. Multiple conditions can set.
        continue
    print(i)

print("Exit Program")
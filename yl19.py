text = "Kuressaare Ametikool"

c = 0

for char in text:
    if char.lower() in "aeiouõüäö":
        c += 1

print(c)
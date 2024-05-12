age = 25
smokes = True

health = "Poor" if age > 60 or smokes else ("Good" if age < 30 else "Fair")

# Equivalent code
if age > 60 or smokes:
    health = "Poor"
else:
    if age < 30:
        health = "Good"
    else:
        health = "Fair"


lst = ["a", "b", "c"]
print(*lst)
print(*lst, sep="-")
print(*lst, sep="-", end=" End of lst\n")

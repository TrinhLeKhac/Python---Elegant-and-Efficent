# immutable: str, int, float, bool, bytes, tuple
# mutable: list, set, dict


x = (1, 2)  # assignment y = x (immutable) => copy values not reference
y = x
x = (1, 2, 3)
print(x, y)


z = [1, 2]  # mutable
t = z   # assign => reference

z[0] = 100  # can change values
print(z, t)


def clone(xs: list[str]) -> list[str]:
    c: list[str] = []
    i: int = len(xs) - 1
    while i >= 0:
        c.append(xs[i])
        i -= 1
    return c


letters: list[str]
school: list[str]

letters = ["U", "N", "C"]
school = clone(letters)

school.append("!")

print(letters[1] == school[1])
# nfinite Even Number Generator (Generators)


def even_numbers():
    num = 2

    while True:
        yield num
        num += 2

n = 5
gen = even_numbers()

for i in range(n):
    print(next(gen))

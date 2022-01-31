counter = 0
for c in range(1,48):
    for b in range (1, c):
        for a in range(1, b):
            if a * a + b * b == c * c:
                counter += 1
                print('{}, {}, {}'.format(a, b, c))
print(f'The count of the Pythagorean triples is {counter}')
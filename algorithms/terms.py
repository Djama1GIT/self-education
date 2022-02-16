integer = int(input())
terms, terms_sum = [1 if integer else 0], 1
while terms_sum+terms[-1] < integer:
    terms += [terms[-1] + 1]
    terms_sum += terms[-1]
if terms_sum < integer:
    terms += [terms.pop(-1) + (integer-terms_sum)]
print(len(terms))
print(*terms)
polynomial = input("Enter a polynomial: ")
k = int(input("Enter k value: "))
terms = []
terms = polynomial.split(" ")
while "+" in terms:
  terms.remove("+")

x = 0
while x != len(terms):
  if terms[x] == "-":
    terms[x] += terms[x+1]
    terms.remove(terms[x+1])
  x += 1

coefficients = []
for x in range(len(terms)):
  term = terms[x]
  for y in range(len(term)):
    if term[y] == "x":
      coefficients.append(int(term[:y]))

quotient = [coefficients[0]]

for x in range(len(coefficients)-1):
  a = quotient[x] * k
  quotient.append(coefficients[x+1] + a)

r = int(terms[-1]) + (quotient[-1] * k)
print(f"Quotient: {quotient}")
print(f'The remainder is {r}')
print(f')
# 2x^3 - 1x^2 - 25x - 12

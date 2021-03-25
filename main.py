###solution to exercise 101 from ben stephenson's 'the python workbook'.

def gcd(x,y):
  d = min(x,y)
  while x % d or y % d:
    d -= 1
  return(d)

def reduce(numerator, denominator):
  gcd_ = gcd(numerator, denominator)
  return numerator // gcd_, denominator // gcd_

numerator, denominator = input('Enter the numerator and denominator: ').split(',')

numerator, denominator = reduce(int(numerator),int(denominator))

print(f'The reduced fraction is {numerator} / {denominator}.')

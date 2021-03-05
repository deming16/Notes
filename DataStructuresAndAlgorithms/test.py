def mul(x,y):
  return x*y

def pow(x,y):
  return x**y

def make_generator(op):
  return lambda y : lambda x : op(x,y)

make_multiplier1 = make_generator(mul)
# lambda y : lambda x : mul(x,y)
make_multiplier2 = make_multiplier1(3)
# lambda 3 : lambda x : mul(x,y)
# lambda x : mul(x,3) --> because 3 is passed into the lambda function
make_multiplier3 = make_multiplier2(2)
# lambda 2: mul(x,3)
# mul(2,3) --> this is not a lambda function, it just executes immediately
# 6
make_exponentiater = make_generator(pow)
print(make_multiplier(3)(2)) # 6
print(make_exponentiater(3)(2)) # 8

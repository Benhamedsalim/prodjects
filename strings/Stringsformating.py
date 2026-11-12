name = "Salim"
age = 30
print("Hello, my name is", name, "and my age is", age, "years old")
print("Hello, my name is %s. and my age is %d years old." % (name, age))

rank = 9.0
print("Hello, my name is %s. and my age is %d years old. my rank is %.2f" % (name, age, rank))
print(f"Hello, my name is {name}. and my age is {age}  years old. my rank is {rank:.3f} " )

print(f"Hello, my name is {name}. and my age is {age+1}  years old. my rank is {rank:.3f} " )

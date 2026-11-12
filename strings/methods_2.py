#starstwith , endswith
test = "Hello world"
print(test.startswith("Hello"))
print(test.startswith("world"))
print(test.endswith("world"))
print(test.endswith("d"))
print(test.startswith("H"))
print(test.startswith("w", 6))

print("-" * 17)

#strip rstrip, lstrip
txt = ("      Hello world      ")
print(txt)
print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())
txt = ("@@@@@@@Hello world@@@@@@@")
print(txt)
print(txt.strip('@'))
print(txt.lstrip('@'))
print(txt.rstrip('@'))

txt = ("@#@#@#@Hello world@#@#@#@")
print(txt)
print(txt.strip('@#'))
print(txt.lstrip('@#'))
print(txt.rstrip('@#'))

print("-" * 17)
#zfill
hour = "1"
min = "9"
sec = "5"
print(f"{hour.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}")
print(f"{hour.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}")

hour = "1"
min = "19"
sec = "25"
print(f"{hour.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}")
print(f"{hour.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}")
# rjust(), ljust(), center()

test = 'Hello'
print(test.rjust(10))
print(test.rjust(10, '#'))
print(test.ljust(10))
print(test.ljust(10, '#'))
print(test.center(10))
print(test.center(11, '#'))
#==========================================================================
print("-" * 17)
#==========================================================================
#expandtabs
test = "Hello \tHow are you \tare you fine"
print(test)
print(test.expandtabs())
print(test.expandtabs(0))
print(test.expandtabs(1))
print(test.expandtabs(10))







import re
def isPhoneNumber(number):
    isphone = re.search(r"\d{3}-\d{3}-\d{4}", number)
    if isphone:
        print(f"The number {number} is a valid phone number")
    else:
        print(f"The number {number} is not a valid phone number")
isPhoneNumber("123-456-6789")

#==================================================================
print("-" * 17)
#==================================================================
#findall

string = """Hello my Number is 415-555-1011 and
my friend's number is 658-984-2165"""

search = re.findall(r"\d{3}-\d{3}-\d{4}", string)
print(search)

test_search = re.findall(r"H", string)
print(test_search)

#practice
phone_number = input("Enter your phone number: ")
search_phone = re.findall(r"\d{3}-\d{3}-\d{4}", phone_number)

list = []

if search_phone == [] :
    print(f"The number {phone_number} is not a valid phone number")
else:
    list.append(search_phone)
    print(f"The number {phone_number} is a valid phone number and is added to the list")


# تبحث الدالة ()search عن أول موقع يحصل فيه تطابق مع التعبير النمطي المُعطى، وتعيد كائن match المقابل.
# تعيد الدالة ()findall جميع حالات التطابق مع التعبير النمطي المُعطى.
# تعيد الدالة ()group سلسلة الأحرف التي تم إيجادها في النص و التي تم تخزينها في كائن match.
# الذي قام باستدعائها.
# تعيد التابع ()span كائن tuble يمثل موضع البداية والنهاية لكائن match الذي تم إيجاده.




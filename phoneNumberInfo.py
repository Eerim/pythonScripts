import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

# get info about phone number
info = phonenumbers.parse("+353858726306", None)
print(info)
print(info.country_code)
print(info.national_number)

# check the number is valid or not - less digit
info = phonenumbers.parse("+35385872636", None)
print(phonenumbers.is_valid_number(info))

# get phone number in a texft
info = "call me +353858726306 on weedays +353858726307 on weekends"
for phnumber in phonenumbers.PhoneNumberMatcher(info, "None"):
    print(phnumber)

# get carrier info
info = phonenumbers.parse("+353858726306")
print(carrier.name_for_number(info, "tr"))

# get carrier info
info = phonenumbers.parse("+35318513322")
print(geocoder.description_for_number(info, "en"))

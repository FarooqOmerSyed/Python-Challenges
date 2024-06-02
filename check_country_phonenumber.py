import phonenumbers
from phonenumbers import geocoder

phoneNum = input("Enter your phone number with country code: ")
phone_number = phonenumbers.parse(phoneNum)
print(geocoder.description_for_number(phone_number, 'en'))
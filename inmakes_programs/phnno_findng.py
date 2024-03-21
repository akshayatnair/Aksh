import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier


phone_number=input("enter the phone number with country code")
#parsing string to the number
pn=phonenumbers.parse(phone_number)
#printing the timezone
tz=timezone.time_zones_for_number(pn)
print("Timezone :",str(tz))
#printing the location
location=geocoder.description_for_number(pn,'en')
print("Location:",str(location))
#printing the service provider
sp=carrier.name_for_number(pn,'en')
print("Service Provider:",str(sp))
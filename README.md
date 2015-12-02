# sampleScrub

##Description##
A sample python script using the twilio lookup service to read a CSV file, format the phone number, determine the type of each number, and write out a new CSV file with the information. 

##Requirements##
You'll need to [install the Twilio Python Helper Library](https://www.twilio.com/docs/python/install) to get started.

Update the script with your Twilio SID and token
```Python
account_sid = "INSERT YOUR ACCOUNT SID HERE"
auth_token = "INSERT YOUR AUTH TOKEN HERE"
```

Lastly, update the column position to read the phone number from
```Python
SOURCE_PHONE_COLUMN = 16
```

##Usage##
```Python
python twiScrub.py
```
from twilio.rest.lookups import TwilioLookupsClient
import csv
import twilio

# Prompt user for sample file to scrub
sampleFile = raw_input('Enter sample file: ')

# Set Twilio account information
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "INSERT YOUR ACCOUNT SID HERE"
auth_token = "INSERT YOUR AUTH TOKEN HERE"

SOURCE_PHONE_COLUMN = 16

# We want to skip the header row
skiprow = 1
with open(sampleFile, 'rU') as csvfile, open(sampleFile + "_new", 'w') as new_csvfile:
    sample = csv.reader(csvfile, delimiter=',', quotechar='|')
    sample_out = csv.writer(new_csvfile, delimiter=',', quotechar='|')
    for row in sample:
        try:
            if skiprow == 1:
                sample_out.writerow(row + ['FromattedPhone']+['PhoneType'])
                skiprow=0
            else:
                client = TwilioLookupsClient(account_sid, auth_token)
                number = client.phone_numbers.get(row[SOURCE_PHONE_COLUMN], include_carrier_info=True)
                print "Phone: %s Type: %s" % (number.national_format, number.carrier['type'])
                sample_out.writerow(row + [number.national_format]+[number.carrier['type']])
        except twilio.TwilioRestException as te:
            print (te)


# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACec719e187bb196bd278f412264266280"
auth_token = "96d1db7a4ced24cee7b3e77b3d22669c"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+573162697465",
                                             from_="+15555555555",
                                             body="Recuerda que tu impuesto IVA Bimensual (Mayo/Junio) se vence en 3 dias. Servicio gratuito de BackStartup.")
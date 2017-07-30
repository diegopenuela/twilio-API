# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACec719e187bb196bd278f412264266280"
auth_token = "96d1db7a4ced24cee7b3e77b3d22669c"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+573162697465",
                                             from_="+14159158454",
                                             body="Diego, recuerda que tu impuesto IVA Bimensual (Mayo/Junio) se vence en 3 dias. Servicio gratuito de BackStartup.")

message = client.api.account.messages.create(to="+573164715235",
                                             from_="+14159158454",
                                             body="Cristian, recuerda que tu impuesto IVA Bimensual (Mayo/Junio) se vence en 3 dias. Servicio gratuito de BackStartup.")

message = client.api.account.messages.create(to="+573103250123",
                                             from_="+14159158454",
                                             body="Adriana, recuerda que tu impuesto IVA Bimensual (Mayo/Junio) se vence en 3 dias. Servicio gratuito de BackStartup.")

message = client.api.account.messages.create(to="+5215534817317",
                                             from_="+14159158454",
                                             body="Juana, recuerda que tu impuesto IVA se vence en 3 dias. Servicio gratuito de BackStartup.")

message = client.api.account.messages.create(to="+573058628798",
                                             from_="+14159158454",
                                             body="Henry, recuerda que tu impuesto IVA Bimensual (Mayo/Junio) se vence en 3 dias. Servicio gratuito de BackStartup.")
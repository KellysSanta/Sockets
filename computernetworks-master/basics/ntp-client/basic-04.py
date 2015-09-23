#!/usr/bin/python
# Este programa pregunta a un servidor NTP por la fecha y la hora y lo imprime
#
import ntplib
from time import ctime

ntp_client = ntplib.NTPClient()
response = ntp_client.request("pool.ntp.org")
print ctime(response.tx_time)

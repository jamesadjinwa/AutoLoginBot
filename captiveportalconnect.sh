#!/usr/bin/env bash

######################################################
# PURPOSE : Auto connect to specific SSID           ##
#                                                   ##
# On Ubuntu copy this file at /etc/network/if-up.d/ ##
#                                                   ##
######################################################

# Set the name of an SSID with a captive portal:
SSID="SSID"

# Don't run on the loopback device
[ "$IFACE" != "lo" ] || exit 0

# Don't run on ethernet
# Check your ethernet interface name(s) - Run `iwconfig` and find options other than "lo" with "no wireless connections." \
# listed. Copy this line for each if there are more than one, replacing "eth0" as appropriate.
# This following line is an attempt at a generic alternative for the next. If your wifi isn't on eth0, switch it as appropriate on line 13.
# [ ${#`iwconfig $IFACE | grep $IFACE | grep "no wireless extensions."`} = 0 ] || exit 0
[ "$IFACE" != "eth0" ] || exit 0

# Only run on matching SSID
ESSID=$(iwconfig $IFACE | grep ESSID | cut -d":" -f2 | sed 's/^[^"]*"\|"[^"]*$//g')
[ "$ESSID" = "$SSID" ] || { echo "Not running script. SSID: $ESSID Expected: $SSID" && exit 0; }

# Only run if can't connect to the internet:
#[[ $(curl https://peromsik.com/scripts/nettest/connection.php) != "ok" ]] || { echo "Not running script; already logged in to $SSID wifi." && exit 0; }

echo "Running login script for \$SSID=$SSID"

# Run your script that logs into the captive portal here.

`/usr/bin/python2.7 script.py`
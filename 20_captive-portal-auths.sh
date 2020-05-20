## On Ubuntu copy this file at /etc/pm/sleep.d/ ##

#!/usr/bin/env bash

case "${1}" in
resume|thaw)
find /etc/network/if-up.d/ -maxdepth 1 -type f -name 'cp-*' | sort | bash
;;
esac

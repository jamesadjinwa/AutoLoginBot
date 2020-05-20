# AutoLoginBot
This bot will help you in automatically logging in you account of the desired website or webpage when run. It basically saves time and energy of typing the username and password again and again.
On ubuntu system, it runs automatically everytime wireless network is up and even when PC comes back from sleep.
P.S. I used it to login into my college's wifi network.

### How to use

1. Enter the website and your username and password in the required to login into the website.
2. Now go to the website/webpage and open the developer tools/Inspect element option.
3. There search the html code corresponding to the html input fields of username, password and submit button as well.
4. Copy the name(or class or id) of that element and paste it in the python code.
5. On ubuntu linux copy `script.py` and `captiveportalconnect.sh` at `/etc/network/if-up.d/` and `20_captive-portal-auths.sh` at `/etc/pm/sleep.d/`
6. Rename `script.py` and `captiveportalconnect.sh` to `cpauth-yourssid` and `cp-yourssid` <br>

```bash
sudo mv /etc/network/if-up.d/script.py /etc/network/if-up.d/cpauth-yourssid
sudo mv /etc/network/if-up.d/captiveportalconnect.sh /etc/network/if-up.d/cp-yourssid
```

7. Change file permissions `sudo chmod 400 /etc/network/if-up.d/cpauth-yourssid` (the file should be read only by root)
8. Run the file.

(Optional)

As I wanted the automation to be a click easy, I created a Automator (only for macOS users) that just runs the python file when clicked.

###### Created by Ritvik Khanna

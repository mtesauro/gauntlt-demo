TEST vuln-17.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located in the String SQL Injection page (vuln-17) exists

It will return a
	- 1 (error) if the vulnerability is present
	- 0 (success) if the vulnerability is fixed (not present)

This test assumes that you have several things installed:

(1)
WebGoat and Gauntlt are installed and are configured with the correct $PATH

(2)
the python request library installed. To install, run this line in a Debian-based system terminal:

$ pip install requests

If you don't have pip, install pip first:
	$ apt-get install python-pip

Or install the request library in some other way

(3)
There is a local proxy running on 127.0.0.1:8000

Testing for vuln-17 can be done by navigating to:
/home/hacker/gauntlt-demo/examples/webgoat/vuln-17

and running the following line:
$	python attack.py

This Gauntlt test was written by Ouyangzheng Huang and Kevin Ong


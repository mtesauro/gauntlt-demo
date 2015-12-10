#vuln-14.attack

This is a [Gauntlt](http://gauntlt.org/) test to check if the vulnerability in Webgoat located at Injection Flaws => XPATH Injection (vuln-14) exists.

It will return the following:
 - 1 (error): if the vulnerability is present within the web application
 - 0 (success): if the vulnerability is fixed (not present within the web application)

**Note:** This vulnerability tests only a single user: Mike.

# How to set up WebGoat 
* Start up your virtual machine and open up a root terminal.
* Run the following curl-bash script to install WebGoat and Gauntlt
```
$ curl -sSL http://bit.ly/1MJ3qNp | bash
```
* Check to make sure WebGoat installed without problems. To do so, you can use WebGoat START to launch WebGoat. This can be found under Applications/Other/WebGoat START or under Applications/Hacking-Lab/WebGoat START.
!(https://raw.githubusercontent.com/aseal134/gauntlt-demo/master/examples/webgoat/vuln-14/Screenshots/HL-Launch-WebGoat.png)
* Check that Gauntlt installed without problems. 
Launch a terminal (normal, not the root terminal) - the normal terminal is under Applications => Accessories => Terminal.  Make sure to source the rvm script so Gauntlt will be in your path or else the Gauntlt won't be in your path.
!(https://raw.githubusercontent.com/aseal134/gauntlt-demo/master/examples/webgoat/vuln-14/Screenshots/HL-Source-rvm.png)
Create a file called gauntlt-test.attack in the initial-test directory with the following contents:
![Step 2](http://res.cloudinary.com/dx4at2j5f/image/upload/v1449532707/CaseStudy/Step1.png)
![Step 3](http://res.cloudinary.com/dx4at2j5f/image/upload/v1449532665/CaseStudy/Step3.png)

When running the following command: 
```
$ source .rvm/scripts/rvm
```
There will be instances in which you will receive the following error: "no such file or directory". In this case, run the following four commands:
```
$ wget -O rvm.key http://pgp.key-server.io/download/0x3804BB82D39DC0E3
$ gpg --import rvm.key
$ curl -sSL https://get.rvm.io | bash -s stable --ruby
$ source /home/hacker/.rvm/scripts/rvm && cd /home/hacker && gem install gauntlt
```
Afterwards, check to make sure that Gauntlt has installed successfully using the above instructions.

##Executing the Attack
* The attack script is written in Python and requires the following libraries: **requests**, **sys**, and **json**. Simply run the following commands to install these libraries.
```
$ sudo pip install requests
$ sudo pip install simplejson
```
* Clone the REPO onto the Desktop for testing purposes.
* To execute the gauntlt attack, simply run:
```
$ gauntlt
```
* To execute an attack on the WebGoat application to exploit the Stage 5: Reflected XSS vulnerability, simply run:
```
$ cd /home/hacker/Desktop/gauntlt-demo/examples/webgoat/vuln-07
$ python attack.py
```

# Other Assumptions
(1) That jerry-curl and jq are installed and available on the $PATH and uses the generic command-line attack.  To install these run the following command on Debian-based systems aka those using .deb packages.

```
$ sudo apt-get install owasp-wte-jerry-curl owasp-wte-jq
```

This assumes you have the OWASP WTE repo setup on the computer running Gauntlt.  If not, it can be added with:

```
$ sudo echo "deb http://appseclive.org/apt/14.04 trusty main" > /etc/apt/sources.list.d/owasp-wte.list
$ sudo wget -q -O - http://appseclive.org/apt/owasp-wte.gpg.key | apt-key add -
```

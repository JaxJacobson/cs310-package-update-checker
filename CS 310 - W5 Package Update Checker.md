# Jax Jacobson
# 9/28/2025
# CS 310 - W5 Package Update Checker
#
### How did you get the list of packages?
# I first used the command "sudo apt update" to make sure the list of packages was up to date. I than used the command "sudo apt list --upgradable" to see which packages need to be upgraded.

### What is the crontab sequence to run the scripts? 
# You first have ot import CronTab from the crontab library. You then have to open up a new crontab and set the command equal to the path of the script.

### Since this script would require root, how do you install a crontab for root?
# I used the command "sudo apt-get install -y cron" to install the crontab.
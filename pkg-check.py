# Jax Jacobson
# 9/27/2025
# Create a cron job for the user that updates the same packages every week.

from crontab import CronTab
import subprocess

def find_list():

    subprocess.run(["sudo", "apt", "update"])
    print()
    list = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)  # output_capture=True capture the terminal's output, and puts it into list.stdout
                                                                                            # text=True returns an output of plaintext and not raw bytes
    lines = list.stdout.splitlines()

    file = open("upgrade_list.txt", "w")                                                    # Creates a temp file
    file.write(str(lines))                                                                       # Puts the upgradable packages into the temp file
    file.close()

def upgrade():

    packages = []

    file = open("upgrade_list.txt")
    lines = file.read()

    for line in lines [1:]:                                                                 # Skips the first line "Listing... Done"
        package = line.split('/')[0]                                                        # Only takes the character in front of the '/'
        packages.append(package)

    file.close()

    for i in packages:
        subprocess.run(["sudo", "apt", "upgrade"], i, ["-y"])                               # -y assumes all of the user's inputs will be yes when prompted


def main():

    find_list()
    
    scheduled_job = upgrade()
    
    cron = CronTab(user = True)                                                 
    new_cronjob = cron.new(command = f"{scheduled_job}")           
    new_cronjob.setall("*", "*", "*", "*", "1")                     

if __name__ == "__main__":
    main()
        

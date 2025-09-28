# Jax Jacobson
# 9/27/2025
# Create a cron job for the user that updates the same packages every week.

from crontab import CronTab
import subprocess
import os

def find_list():
 
    subprocess.run(["sudo", "apt", "update"])
    print()
    list = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)  # output_capture=True capture the terminal's output, and puts it into list.stdout
                                                                                            # text=True returns an output of plaintext and not raw bytes
    lines = list.stdout.splitlines()

    with open("upgrade_list.txt", "w") as file:                                             # Creates a temp file
        file.write("\n".join(lines))                                                        # Joins all of the packages together and then separates them with a \n


def upgrade():

    packages = []

    with open("upgrade_list.txt") as file:
        lines = file.readlines()

    for line in lines [1:]:                                                                 # Skips the first line "Listing... Done"
        package = line.split('/')[0]                                                        # Only takes the character in front of the '/'
        packages.append(package)



    for i in packages:
        subprocess.run(["sudo", "apt", "upgrade", i, "-y"])                                 # -y assumes all of the user's inputs will be yes when prompted


def main():

    marker = "first_run_done.flag"

    if not os.path.exists(marker):                                                          # Creates a marker to make sure that find_list() only runs once
        find_list()
        with open (marker, "w") as f:
            f.write("done")
    
    upgrade()
    
    cron = CronTab(user = True)                                                 
    new_cronjob = cron.new(command = "python3 /workspaces/cs310-package-update-checker/pkg-check.py")           
    new_cronjob.setall("* 5 * * 1")
    cron.write()                     

if __name__ == "__main__":
    main()
        

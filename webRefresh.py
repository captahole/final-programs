#Write a script in python that will refresh a website in the current tab randomly from 30 seconds to two minutes


import random
import time
import webbrowser

def refresh_website():
    while True:
        # Generate a random time interval between 30 seconds and 2 minutes
        refresh_time = random.randint(30, 120)
        
        # Wait for the generated time interval
        time.sleep(refresh_time)
        
        # Refresh the website
        webbrowser.open_new_tab('https://jetblue.flica.net/full/otframe.cgi?BCID=014.155&ViewOT=1')  # Replace with your desired website URL

# Call the function to start refreshing the website
refresh_website()

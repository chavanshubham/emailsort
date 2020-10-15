# emailsort
Create Labels and sort matching emails into the label based on subject lines. You can choose the label name, the subject filter text to use, the type of check i.e. exact match or containing the entered phrase.

# SETUP GUIDE:

Python3 is used for this project. Install python3 on your machine and use the python3 command to run the script. The script also uses the Gmail API to access gmail data.

# 1. Download and install Python3 on your machine.

Please refer to any Python3 installation guide.

# 2. GMAIL API USING QUICKSTART.

Google usually offers a quickstart guide to make authorization easier. This process has a few limitations but is enough for our purposes. The other way to get the API key is to create a new project, which is a bit trickier.

Python Quickstart: https://developers.google.com/gmail/api/quickstart/python

Follow the instructions on the above page to get done with the GMAIL API setup. Namely:

Step 1. Turn on the GMail API by clicking on the "Enable Gmail API" button.

Step 2. Login to your Gmail account, name your project, select desktop app if prompted.

Step 3. Click on "Download Credentials". A file by the name credentials.json will be downloaded. Save this in your working directory.

# 3. Install Google client library.

You can do this using pip. Run the following command in your terminal. 

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# 4. Setup the google sample and test.

Create a python file called quickstart.py in the same directory, copy the Python Quickstart sample code.

# 5. Run the code

Run the code with the following command

python3 quickstart.py

# 6. Allow unsecured access as the app is in development phase. 

You will be redirected to the web browser. Login to your gmail account. A warning saying that the app is not verified will be shown. This is as expected as we are using the quickstart method, our app is not yet verified. Click on Advanced > Go to {Project Name} (unsafe).

# 7. Allow permissions.

Grant the required permissions. The code should now be working on your terminal. If not, refer to Google Quickstart's Troubleshooting guide by scrolling down on the page. 

# 8. Run the emailsort script.

Step 1. Remove token.pickle from the working directory. 

Step 2. Save the emailsort.py to your working directory.

Step 3. Run the following command on your terminal through the working directory

python3 emailsort.py

Step 4. Log in to your email account, grant the required permissions.

You will get a message saying the permissions have been granted. The code should now be working.

# 8. To change the email account or the permissions, delete the token.pickle file and rerun the script.

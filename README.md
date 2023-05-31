# Utility tool
1. Return company name from Mac Address
2. ToDo

# Running the tool

You must have docker installed and running

Run: docker build . -t macaddresstool

Run: docker images 

Get the IMAGE ID (Image_ID)

Run: mkdir ~/workdir

Run: docker run -v ~/workdir:/etc/workdir  -t Image_ID 

Enter the Mac Address and click enter

The company name will be displayed as follows

Company name for the Mac Address 44:38:39:ff:ef:57 is Cumulus Networks, Inc

# ToDo
Request authentication and encryption
Create Package 
Create Docker Compose file
Push image to registry

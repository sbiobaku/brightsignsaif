# Utility tool
1. Return company name from Mac Address
2. ToDo

# Create the Image

Run: git clone git@github.com:sbiobaku/brightsignsaif.git

Run: cd brightsignsaif/

Run: docker build . -t macaddresstool

# Running the script

Run: docker images 

Get the IMAGE ID (Image_ID)

Run: docker  run -w /etc/workdir -i -t  Image_ID  python3 allDataFeedMac.py --MacAddress 44:38:39:ff:ef:57

The company name will be displayed as follows

Company name for the Mac Address 44:38:39:ff:ef:57 is Cumulus Networks, Inc

# ToDo
Request authentication and encryption
Create Python package 
Create Docker Compose file if needed
Push image to registry

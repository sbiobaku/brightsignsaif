# Utility tool
1. Return company name from Mac Address
2. ToDo


# Running the tool
Run: docker build . -t macAddressTool

Run: docker images 

Get the image Id (Image_ID)

The working directory should be set up on local machine as ~/workdir

Run: docker run -v ~/workdir:/etc/workdir  -t Image_ID

cd ~/workdir

Run: python3 allDataFeedMac.py 

Enter the Mac Address and click enter

The company name will be displayed as follows

Company name for the Mac Address 44:38:39:ff:ef:57 is Cumulus Networks, Inc

# ToDo
Request authentication and encryption
Create Package 
Push image to registry

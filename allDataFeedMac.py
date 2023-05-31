import requests
import argparse

sessionRequests = requests.Session() 
url = "https://mac-address.alldatafeeds.com"


def getCompanyNameFromMac (macAddress):
    macUrl = url+"/api/mac-address/lookup/"
    payload = {"mac-address": macAddress}
    
    res = sessionRequests.post(macUrl, json = payload)
    if not (res.status_code == 200):
         print(f"The status code for the request you made was {res.status_code}")
    else:
         dataJson = res.json()

    companyNa = getReportDetails(dataJson['report_id'])
    return companyNa
  

def getReportDetails(reportId):
    urlReport = url+"/_next/data/Tf9pzEFow9scQ87pOfWw3/mac-address-lookup/"+reportId+".json?id="+reportId
    report = {}

    res = sessionRequests.get(urlReport)
    if res.status_code == 200:
          report = res.json()
    else:
          print(f"The status code of {res.status_code} was returned for report Id {reportId}")
    companyN = report["pageProps"]["lookupResults"]["vendorDetails"]["companyName"]
    return companyN
  
  
if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('--MacAddress', type=str, required=True)
     args = parser.parse_args()
     companyName  = getCompanyNameFromMac(args.MacAddress)
     print(f"Company name for the Mac Address {args.MacAddress} is {companyName}")


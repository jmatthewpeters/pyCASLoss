import numpy as np
import pandas as pd

class ClaimType(object):
    df_columns = ["claimid", "lob", "type", "status", "occurrencedate", 
                    "reportdate", "incurring", "osratio", "settlementdate", "totalloss", "ultimateloss", 
                    "deductible", "limit", "paid", "lae", "claimliability", "expectedloss", "ultimatelae", 
                    "expectedlae", "reopendate", "reopenloss", "sim", "stringsasfactors"]
    #@slot simno The simulation index.
    #line A string to identify the business line that the claim belongs to.
    #claimType A string to identify the type of the claim. It further classifies the claims within a business line. For example, the type could be based on the size of the loss. 
    #iRBNER A Boolean variable to indicate whether RBNER (open claims) should be simulated.
    #iROPEN A Boolean variable to indicate whether claim reopen should be simulated.
    #iIBNR A Boolean variable to indicate whether IBNR claims should be simulated.
    #iUPR A Boolean variable to indicate whether future claims should be simulated.
    #fIBNER IBNER development factor.
    #severity Severity distribution.
    #frequency Frequency distribution.
    #reportLag Report lag distribution.
    #settlementLag Settlement lag distribution.
    #reopen Claim reopen probability based on the number of years after settlement till valuation date.
    #reopenLag Reopen lag distribution.
    #resettleLag Resettlement lag distribution.
    #roDevFac Reopened claim development factor.
    #ioDevFac A numeric variable to indicate the method of loss development for open claim severity. 1: Conditional distribution based on paid loss; 2: conditional distribution based on incurred loss; 3: year-to-year development factors
    #irDevFac A numeric variable to indicate the method of loss development for claim reopen severity simulation. 1: Conditional distribution based on paid loss; 2: conditional distribution based on incurred loss; 3: year-to-year development factors
    #freqIndex Frequency distribution time index.
    #severityIndex Severity distribution time index.
    #exposureIndex Exposure time index for IBNR or UPR.
    #iCopula Whether copula is used to model severity, report lag and settlement lag.
    #ssrCopula Copula object used for severity, report lag and settlement lag.
    #sdata Indicating whether only closed claims (CLOSED) or closed + open claims (ALL) will be used for severity fitting.
    #p0 An yearly table that controls the probability of invalid claim, excluding these valid claims less than deductible based on development year. It is based on the DevFac class.

    def __init__(self, simno, line, claimtype, irbner, iropen, iibnr, iupr):
        self.simno = simno
        self.line = line
        self.severity = ""
        self.frequecy = ""
        self.reportlag = ""
        self.settlementlag = ""
        self.reopen = ""
        self.reopenlag = ""
        self.resettlelag = ""
        self.rodevfac = None
        self.iodevfac = 0
        self.irDevFac=0
        self.irbner = irbner 
		self.ibnrfreqIndex=1
		self.uprfreqindex=1
		self.severityindex=1
		self.exposureindex=1
		self.icopula=False
		self.ssrcopula=Copula()
		self.laedevfac=0
		self.deductible=0
		self.limit=""
		self.sdata="CLOSED"
		self.p0=0

    
        def claimSample(self, claimdata, startdate, enddate):
            #if len(claimdata)>0:
                #data cleaning stuff





            if self.irbner == True:
                if len(claimdata) == 0:
                    nobs = 0
                    tmpdata = pd.DataFrame(columns=df_columns)
                    return tmpdata
                else:
                    tmpdata = claimdata[claimdata["status"] == "OPEN"]


        def irbner(self, claimdata, evaluationdate):
            if len(claimdata)==0:
                nobs=0
            else:
                tmpdata = claimdata[claimdata["status"]=="OPEN" | claimdata["settlementdate"] > evaluationdate ]
                settlementdates = pd.to_datetime(tmpdata["reportdate"]) + pd.DataFrame([pd.to_datetime(claimsdata["AccidentDate"]) - pd.to_datetime(claimsdata["ReportDate"]), pd.to_datetime("2019-04-17") - pd.to_datetime(claimsdata["ReportDate"])]).min()



            pass
        
        def iropen(self):
            pass
        
        def iibnr(self):
            pass

        def iupr(self):
            pass

        

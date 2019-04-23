#imports claim data from file
import numpy as np
import pandas as pd

'''
DataField       Use	Match Field	Required Format
ClaimNo	        Yes	ClaimID	numchar
AccidentDate	Yes	occurrenceDate	yyyy-mm-dd
ReportDate	    Yes	reportDate	yyyy-mm-dd
Line	        Yes	LoB	numchar
Type	        Yes	Type	numchar
ClaimLiability  Yes	claimLiability	TRUE/FALSE
Limit	        Yes	Limit	num
Deductible	    Yes	Deductible	num
TotalPayment	No		
PaymentDate	    No		
CloseDate	    Yes	settlementDate	yyyy-mm-dd
Status	        Yes	status	OPEN/CLOSED
reportedCount   No		
closedPaidCount No		
closedUnPaidCount  No		
openCount       No		
Paid            Yes	Paid	num
Outstanding	    No		
Incurred	    Yes	incurredLoss	num
'''


def load_claimdata(datafile, filetype='csv'):
    if filetype == 'csv':
        claimdata = pd.read_csv(datafile)
        claimdata['AccidentDate'] = pd.to_datetime(claimdata['AccidentDate'])
        claimdata['ReportDate'] = pd.to_datetime(claimdata['ReportDate'])
        claimdata['PaymentDate'] = pd.to_datetime(claimdata['PaymentDate'])
        claimdata['CloseDate'] = pd.to_datetime(claimdata['CloseDate'])

    else:
        claimdata = pd.read_excel()

    return claimdata
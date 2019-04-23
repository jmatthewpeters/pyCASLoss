import numpy as np
import pandas as pd
import math

class Triangle(object):
    '''
    #' An S4 class to represent a triangle or rectangle object.
    #'
    #' triID A character string to identify the triangle object.
    #' type A character string that indicates the triangle type, such as reportedCount, closedCount, paidLoss, and incurredLoss.
    #' startDate The start date for the accident year or Quarter.
    #' frequency A character that indicates the frequency of the triangle, "yearly" or "quarterly".
    #' sim A number that indicates the simulation number used to complete the rectangle. Zero means using the average value.
    #' percentile A number that indicates the percentile used to complete the rectangle. It is only used when sim is NA. 
    #' iRBNER A Boolean that indicates whether open claims are simulated. If not, current information will be used for constructing rectangles. Otherwise, simulated data will be used. 
    #' iROPEN A Boolean that indicates whether claim reopen are simulated. If not, current information will be used for constructing rectangles. Otherwise, simulated data will be used. 
    #' percentile A number that indicates the percentile used to complete the rectangle. It is only used when sim is NA. 
    #' upper A matrix that contains the upper triangle based on claim data.
    #' upperkeep A matrix that contains the upper triangle that are not simulated. It will be used to construct the rectangle for the non-simulated part.
    #' rectangle A matrix that contains the entire rectangle based on simulation data.
    claimsdata is a pandas dataframe with 
    '''

    def __init__(self, triid, type, startDate, evalutiondate, frequency, sim, percentile, iRBNER, 
                iROPEN):
        self.triID = triid
        self.type = type
        self.startDate = startDate #datatime
        self.evalutiondate = evalutiondate #datetime
        self.frequency = frequency #string
        self.sim = sim #integer
        self.percentile = percentile #interger
        self.iRBNER = iRBNER #bool
        self.iROPEN = iROPEN #bool
        self.upper = np.empty() #numpy array
        self.upperkeep = np.empty() #numpy array
        self.rectangle = np.empty()  #numpy array
        self.startyear = 2018
        self.endyear = 2028
        self.startmonth = 1
        self.endmonth = 1
        self.startquarter = 1
        self.endquarter = 1
        self.claimsdata
        self.rownames = []
        self.colnames = []

    def set_rectangle_size(self):
        '''sets the size of the rectangle
        '''
        startyear = self.startDate.year()
        endyear = self.evaluationdate.year()
        startmonth = self.startDate.month()
        endmonth = self.evaluationdate.month()
        startquarter = math.ceil(startmonth / 3)
        endquarter = math.ceil(endmonth / 3)

        if self.frequency == "yearly":
            numbercols = endyear - startyear + 1
            rownames = [n for n in range(startyear, endyear + 1)] # may need to make sure this does what c()
            colnames = [f"M{n*12}" for n in range(1, numbercols+1)]
        else: 
            numbercols = (endyear - startyear) * 4 + endquarter - startquarter  +1
            rownames = []
            for i in range(startyear, endyear +1):
                if i == startyear:
                    for j in range(startquarter, 5):
                        rownames.append(f"{j}Q{i}")
                elif i == endyear:
                    for j in range(1, endquarter+1):
                        rownames.append(f"{j}Q{i}")
                else:
                    for j in range(1,5):
                        rownames.append(f"{j}Q{i}")
            colnames = [[f"m{n*3}" for n in range(1, (numbercols)+1)]]

        self.rectangle = np.zeros((ncols, ncols), dtype=float)



    #' @title Set up the upper triangle based on claim data.
    #' @description
    #' \code{setUpperTriangle} sets up the upper triangle based on a data file.
    #' @param object Triangle Object
    #' @param data Claim Data
    #' @param evaluationDate Evaluation Date
    #' @param lob Line of Business
    #' @param ctype Claim Type
    #' @examples
    #' library(cascsim)
    #' data(claimdata)
    #' xTri <- new("Triangle", triID = "TRI1", type = "reportedCount", startDate=as.Date("2012-01-01"), frequency="yearly", sim=1, percentile=50)
    #' xTri<-setUpperTriangle(xTri,claimdata)
    #' xTri@upper
    #' 
    #' xTri <- new("Triangle", triID = "TRI1", type = "closedCount", startDate=as.Date("2012-01-01"), frequency="quarterly", sim=1, percentile=50)
    #' xTri<-setUpperTriangle(xTri,claimdata)
    #' xTri@upper
    #'
    #' xTri <- new("Triangle", triID = "TRI1", type = "incurredLoss", startDate=as.Date("2012-01-01"), frequency="yearly", sim=1, percentile=50)
    #' xTri<-setUpperTriangle(xTri,claimdata,lob="Auto",ctype="H")
    #' xTri@upper
    #'
    #' xTri <- new("Triangle", triID = "TRI1", type = "paidLoss", startDate=as.Date("2012-01-01"), frequency="yearly", sim=1, percentile=50)
    #' xTri<-setUpperTriangle(xTri,claimdata,lob="Auto",ctype="H")
    #' xTri@upper
    #'
    #' @rdname setUpperTriangle
    #' @export
    def setUpperTriangle(self, claimsdata, evaluationdate, lob="Total", ctype="Total"):
        '''sets up the upper triangle based on the claims data file
        '''
        data = {}
        data['lob'] = lob
        data['type'] = ctype

        if lob != "Total":
            data["lob"] = lob

        if ctype != "Total":
            data["type"] = ctype

        startyear = self.startDate.year()
        endyear = evaluationdate.year()
        startmonth = self.startDate.month()
        endmonth = evaluationdate.month()
        startquarter = math.ceil(startmonth / 3)
        endquarter = math.ceil(endmonth / 3)

        if self.frequency == "yearly":
            numbercols = endyear - startyear + 1
            rownames = [n for n in range(startyear, endyear + 1)] # may need to make sure this does what c()
            colnames = [f"M{n*12}" for n in range(1, numbercols+1)]
        else: 
            numbercols = (endyear - startyear) * 4 + endquarter - startquarter  +1
            rownames = []
            for i in range(startyear, endyear +1):
                if i == startyear:
                    for j in range(startquarter, 5):
                        rowname.append(f"{j}Q{i}")
                elif i == endyear:
                    for j in range(1, endquarter+1):
                        rowname.append(f"{j}Q{i}")
                else:
                    for j in range(1,5):
                        rowname.append(f"{j}Q{i}")
            colnames = [[f"m{n*3}" for n in range(1, (numbercols)+1)]]

        rec = np.zeros((ncols, ncols), dtype=float)

        if "Sim" in claimsdata.columns:
            sim = claimsdata["Sim"]
            data = claimsdata[claimsdata['Sim']==sim]
        
        accidentyears = data["AccidentDate"].dt.year
        accidentmonths = data["AccidentDate"].dt.month
        accidentquarters = math.ceil(accidentmonths / 3)

        if self.frequency == "yearly":
            data['rowno'] = accidentyears - startyear +1
        else:
            data['rowno'] = (accidentyears - startyear) * 4 + (accidentquarters - startquarter) + 1

        if self.type  == 'reportedCount':
            reportyears = data['reportedDate'].dt.year
            reportmonth = data['reportedDate'].dt.month
            reportquarters = math.ceil(reportmonth / 3)
            if self.frequency == "years":
                data['colno'] = (reportyears - accidentyears) + 1
            else:
                data['colno'] = (reportyears - accidentyears) * 4 + (reportquarters - accidentquarters) + 1
        
        elif self.type == 'closedCount':
            
            settleyears = data["settlementDate"].dt.year
            settleyears = settleyears.fillna(endyear + 1)
            settlemonths = data['settlementDate'].dt.month
            settlemonths = settlemonths.fillna(endmonth)
            if self.frequency == 'yearly':
                data['colno'] = (settleyears - accidentyears) + 1
            else:
                data['colno'] = (reportyears - accidentyears) * 4 + (reportquartes - accidentquarters)
        
        else:
            settleyears = data["settlementDate"].dt.year
            settleyears = settleyears.fillna(endyear)
            settlemonths = data['settlementDate'].dt.month
            settlemonths = settlemonths.fillna(endmonth)
            if self.frequency == 'yearly':
                data['colno'] = (settleyears - accidentyears) + 1
            else:
                data['colno'] = (reportyears - accidentyears) * 4 + (reportquartes - accidentquarters)
        
        #aggregate claims data into 
        if self.type == "reportedCount" or self.type == "closedCount":
            agg = data[['occurrenceDate','rowno', 'colno']].groupby(['rowno', 'colno']).count()
        elif self.type == "incurredLoss":
            agg = data[['incurredLoss','rowno', 'colno']].groupby(['rowno', 'colno']).sum()
        else:
            agg = data[['Paid','rowno', 'colno']].groupby(['rowno', 'colno']).sum()


        for row in range(1, length(rowname)):
            rowsum = 0
            for col in range(1, ncols):
                temp = agg[(agg['rowno'] == row) & (agg['colno'] == col)]
                if temp != None:
                    rowsum = rowsum + temp

                rec[row-1, col-1] = rowsum
        
        self.upper = rec

    def setupperkeep(self, claimsdata, evaluationdate, lob="Total", type="Total"):
        '''Set the upper tainal for non-simulated data
        '''
        data = {}
        data['lob'] = lob
        data['type'] = ctype

        if lob != "Total":
            data["lob"] = lob

        if ctype != "Total":
            data["type"] = ctype

        startyear = self.startDate.year()
        endyear = evaluationdate.year()
        startmonth = self.startDate.month()
        endmonth = evaluationdate.month()
        startquarter = math.ceil(startmonth / 3)
        endquarter = math.ceil(endmonth / 3)

        if self.frequency == "yearly":
            numbercols = endyear - startyear + 1
            rownames = [n for n in range(startyear, endyear + 1)] # may need to make sure this does what c()
            colnames = [f"M{n*12}" for n in range(1, numbercols+1)]
        else: 
            numbercols = (endyear - startyear) * 4 + endquarter - startquarter  +1
            rownames = []
            for i in range(startyear, endyear +1):
                if i == startyear:
                    for j in range(startquarter, 5):
                        rowname.append(f"{j}Q{i}")
                elif i == endyear:
                    for j in range(1, endquarter+1):
                        rowname.append(f"{j}Q{i}")
                else:
                    for j in range(1,5):
                        rowname.append(f"{j}Q{i}")
            colnames = [[f"m{n*3}" for n in range(1, (numbercols)+1)]]

        rec = np.zeros((ncols, ncols), dtype=float)

        if "Sim" in claimsdata.columns:
            sim = claimsdata["Sim"]
            data = claimsdata[claimsdata['Sim']==sim]
        
        accidentyears = data["AccidentDate"].dt.year
        accidentmonths = data["AccidentDate"].dt.month
        accidentquarters = math.ceil(accidentmonths / 3)

        if self.frequency == "yearly":
            data['rowno'] = accidentyears - startyear +1
        else:
            data['rowno'] = (accidentyears - startyear) * 4 + (accidentquarters - startquarter) + 1

        if self.type  == 'reportedCount':
            reportyears = data['reportedDate'].dt.year
            reportmonth = data['reportedDate'].dt.month
            reportquarters = math.ceil(reportmonth / 3)
            if self.frequency == "years":
                data['colno'] = (reportyears - accidentyears) + 1
            else:
                data['colno'] = (reportyears - accidentyears) * 4 + (reportquarters - accidentquarters) + 1
        
        elif self.type == 'closedCount':
            
            settleyears = data["settlementDate"].dt.year
            settleyears = settleyears.fillna(endyear + 1)
            settlemonths = data['settlementDate'].dt.month
            settlemonths = settlemonths.fillna(endmonth)
            if self.frequency == 'yearly':
                data['colno'] = (settleyears - accidentyears) + 1
            else:
                data['colno'] = (reportyears - accidentyears) * 4 + (reportquartes - accidentquarters)
        
        else:
            settleyears = data["settlementDate"].dt.year
            settleyears = settleyears.fillna(endyear)
            settlemonths = data['settlementDate'].dt.month
            settlemonths = settlemonths.fillna(endmonth)
            if self.frequency == 'yearly':
                data['colno'] = (settleyears - accidentyears) + 1
            else:
                data['colno'] = (reportyears - accidentyears) * 4 + (reportquartes - accidentquarters)
        
        #aggregate claims data into 
        if self.type == "reportedCount" or self.type == "closedCount":
            agg = data[['occurrenceDate','rowno', 'colno']].groupby(['rowno', 'colno']).count()
        elif self.type == "incurredLoss":
            agg = data[['incurredLoss','rowno', 'colno']].groupby(['rowno', 'colno']).sum()
        else:
            agg = data[['Paid','rowno', 'colno']].groupby(['rowno', 'colno']).sum()


        for row in range(1, length(rowname)):
            rowsum = 0
            for col in range(1, ncols):
                temp = agg[(agg['rowno'] == row) & (agg['colno'] == col)]
                if temp != None:
                    rowsum = rowsum + temp

                rec[row-1, col-1] = rowsum
        
        self.upperkeep = rec

    def set_rectangle(self, simdata, evalutiondate, lob, ctype):
        '''sets up the rectangle based on a data file.
        '''
        data = {}
        if lob != "Total":
            data["lob"] = lob

        if ctype != "Total":
            data["type"] = ctype

        if self.sim > 0:
            data["sim"] = self.sim
        else:
            ultagg = simdata[['ultimateloss', 'sim']].groupby('sim').sum()
            nsim = len(ultagg)
            lsim = max(1, math.floor(nsim * self.percentile/100))
            usim = max(1, math.ceil(nsim * self.percentile/100))
            lambda_ = usim - nsim * self.percentile / 100
            lsim = ultagg.loc(lsim)
            usim = ultagg.loc(usim)

        if len(data)<=0:
            #No data available for rectabnle construction.
            return
        else:
            settleyears = simdata["settlementdata"].dt.year
            resettleyears = simdata["resettledate"].dt.year
            settlemonths = simdata['settlementdate'].dt.month
            resettlemonths = simdata['resettledate'].dt.month
            settleyears = settleyears.fillna(resettleyears) 
            settlemonths = settleyears.fillna(resettlemonths)
            settlequarters = np.ceil(settlemonths/3)

            startyear = self.startDate.year
            endyear = settleyears.max()
            evaluationyear = evalutiondate.year
            futureyear = futuredate.year
            startmonth = self.startDate.month
            endmonth = settlemonths.max()
            evaluationmonth = evalutiondate.month
            futuremonth = futuredate.month
            startquarter = math.ceil(startmonth / 3)
            endquarter = math.ceil(endmonth / 3)
            evaluationquarter = math.ceil(evaluationmonth / 3)
            futurequarter = math.ceil(futuremonth / 3)

            if self.frequency == "yearly":
                ncols = endyear - startyear +1
                nevals = evalutionyear - startyear +1
                nrows = futureyear - startyear +1
                rownames = [year for year in range(startyear, endyear +1)]
                colnames = [f"M{n*12}" for n in range(1, numbercols+1)]
            else:
                nvols = (endyear - startyear)*4 + endquarter - startquarter + 1
                nevals = (evaluationyear - startyear)*4 + evaluationquarter - startquarter + 1
                nrows = (futureyear - startyear)*4 + futurequarter - startquarter + 1
                rowname = []
                for i in range(startyear, endyear+1):
                    if i == startyear:
                        for j in range(1,startquarter+1):
                            rowname.append(f"{j}Q{i}")
                    elif i == futureyear:
                        for j in range(1,startquarter+1):
                            rowname.append(f"{j}Q{i}")
                    else:
                        for j in range(1,5):
                            rowname.append(f"{j}Q{i}")
        
        rec = np.zeros((nrows,ncols))

        nsims = 1
        if self.sim != 0:
            #if there is a simulation
            if self.sim > 0:
                simdata["sim"] = self.sim
                nsims = 1
            else:
                nsims = len(data["Sim"])
            
            data = simdatadata[["occurrenceDate","reportDate","settlementDate","ultimateLoss","Paid"]]

            data["accidentyears"] = data["occurrenceDate"].dt.year
            data['accidentmonths'] = data["occurrenceDate"].dt.month
            data['accidentquarters'] = np.ceil(data["accidentmonths"]/3)

            if self.frequency == "yearly":
                data["rowno"] = (data["accidentyears"] - startyear) +1
            else:
                data["rowno"] = (data["accidentyears"] - startyear) * 4 + (data['accidentquarters'] - startquarter) +1

            if self.type == "reportedcount":
                data["reportyears"] = data["reportdate"].dt.year
                data["reportquarters"] = np.ceil(data["reportdate"].dt.month / 3)
                
                if self.frequency == "yearly":
                    data["colno"] = (data['reportyears'] - data['accidentyears']) + 1
                else:
                    data["colno"] = (data['reportyears'] - data['accidentyears']) * 4 + (data["reportquarters"] - data['accidentquarters']) + 1

            else: #settled count
                data['settleyears'] = data['settlementdate'].dt.year
                data['settleyears'] = pd.isnan(data['settleyears'], endyear)
                data['settlequarters'] = np.ceil(data['settlementdate'].dt.month / 3)
                if self.frequency == "yearly":
                    data["colno"] = (data['settleyears'] - data['accidentyears']) + 1
                else:
                    data["colno"] = (data['settleyears'] - data['accidentyears']) * 4 + (data["settlequarters"] - data['accidentquarters']) + 1

            
            if self.type == "reportedCount" or self.type == "closedCount":
                agg = data[['occurrenceDate','rowno', 'colno']].groupby(['rowno', 'colno']).count()
        
            else:
                agg = data[['ultimateloss','rowno', 'colno']].groupby(['rowno', 'colno']).sum()

            for row in range(1, length(rowname)):
                rowsum = 0
                for col in range(1, ncols):
                    temp = agg[(agg['rowno'] == row) & (agg['colno'] == col)]
                    if temp != None:
                        rowsum = rowsum + temp

                    rec[row-1, col-1] = rowsum
            
            for i in range(1, length(rowname)):
                for j in range(1, len(colnames)):
                    rec[i-1,j-1] = rec[i,j] /nsims
            #this whole block should be 
            #rec = rec / nsims
            #rec is a numpy array

            if not self.upperkeep.isnan().any().any():
                for i in range(len(rowname)):
                    if i <= len(self.upperkeep):
                        addtemp = self.upperkeep[i, len(self.upperkeep[0])]
                    else:
                        addtmp = 0
                    for j in range(1,len(colname)):
                        rec[i-1, j-1] = rec[i-1, j-1] + addtmp
        
        else:
            #if there is no simulation
            data = simdata[simdata["sim"]==lsim or simdata["sim"]==usim]
            data = data[["occurrenceDate","reportDate","settlementDate","ultimateLoss","Sim"]]
            data["accidentyear"] = data["occurrencedate"].dt.year
            data["accidentmonth"] = data["occurrencedate"].dt.year
            data['accidentquarter'] = np.ceil(data['accidentmonth'] / 3)

            if self.frequency == "yearly":
                data["rowno"] = (data["accidentyears"] - startyear) +1
            else:
                data["rowno"] = (data["accidentyears"] - startyear) * 4 + (data['accidentquarters'] - startquarter) +1

            if self.type == "reportedcount":
                data["reportyears"] = data["reportdate"].dt.year
                data["reportquarters"] = np.ceil(data["reportdate"].dt.month / 3)
                
                if self.frequency == "yearly":
                    data["colno"] = (data['reportyears'] - data['accidentyears']) + 1
                else:
                    data["colno"] = (data['reportyears'] - data['accidentyears']) * 4 + (data["reportquarters"] - data['accidentquarters']) + 1

            else: #settled count
                data['settleyears'] = data['settlementdate'].dt.year
                data['settleyears'] = pd.isnan(data['settleyears'], endyear)
                data['settlequarters'] = np.ceil(data['settlementdate'].dt.month / 3)
                if self.frequency == "yearly":
                    data["colno"] = (data['settleyears'] - data['accidentyears']) + 1
                else:
                    data["colno"] = (data['settleyears'] - data['accidentyears']) * 4 + (data["settlequarters"] - data['accidentquarters']) + 1

            
            if self.type == "reportedCount" or self.type == "closedCount":
                lagg = data[data["sim"==lsim]][['occurrenceDate','rowno', 'colno']].groupby(['rowno', 'colno']).count()
                uagg = data[data["sim"==usim]][['occurrenceDate','rowno', 'colno']].groupby(['rowno', 'colno']).count()
            else:
                lagg = data[data["sim"==lsim]][['ultimateloss','rowno', 'colno']].groupby(['rowno', 'colno']).sum()
                uagg = data[data["sim"==usim]][['ultimateloss','rowno', 'colno']].groupby(['rowno', 'colno']).sum()

            for i in range(1, len(colname)):
                rowsum  = 0
                for j in range(1, len(colname)):
                    ltmp = lagg[(lagg['rowno'] == i) & (lagg['colno'] == j)]
                    utmp = uagg[(uagg['rowno'] == i) & (uagg['colno'] == j)]
                    tmp = 0
                    if not ltmp.isnan():
                        tmp = lambda_ * ltmp
                    if not utmp.isnan():
                        tmp = tmp + (1-lambda_) * utmp
                    if not tmp.isnan():
                        rowsum = rowsum + tmp
                    
                    rec[i-1, j-1] = rowsum

            if not self.upperkeep.isnan().any().any():
                for i in range(1, len(rowname)):
                    if i <= len(self.upperkeep):
                        addtemp = self.upperkeep[i, len(self.upperkeep[0])] - rec[i, len(self.upperkeep) - i +1]
                    else:
                        addtmp = 0
                    for j in range(1,len(colname)):
                        rec[i-1, j-1] = rec[i-1, j-1] + addtmp







    def tostring(self):
        '''returns rectangle
        '''
        return self.rectangle

import numpy as np
from math import ceil
#' class to represent a time index for frequency or severity distribution.
#'
#' indexID A string to identify the index.
#' startDate The date the index starts. It is expected to be consistent with the start date of the claim analysis.
#' tabulate A boolean to indicate whether the index is determined by a constant rate (FALSE) or a series of index values (TRUE).
#' annualizedRate A yearly index growth rate. It is only used when tabulate == FALSE.
#' yearlyIndex A vector that contains index value on a yearly basis.
#' monthlyIndex A vector that contains index value on a monthly basis. 
#' seasonality A vector that contains seasonal adjustment factor on a monthly basis. 


class index(Object):
    def __init__(self, indexid, startdate, tabulate, annualizedrate, yearlyindex, monthlyindex, seasonality):
        self.indexid = indexid
        self.startdate = startdate
        self.tabulate = tabulate
        self.annualizedrate = annualizedrate
        self.yearlyindex = yearlyindex # np array
        self.monthlyindex = monthlyindex #np array
        self.seasonality = seasonality

    def setid(self, indexid):
        self.indexid = indexid

    def setstartdate(self, startdate):
        self.startdate = startdate

    def settabulate(self, booltabulate):
        # determine whether the index values are constucted from a constant rate or prvided directly
        self.tabulate = booltabulate

    def setannualizedrate(self, annualizedrate):
        self.annualizedrate = annualizedrate

    def setyearlyindex(self, yearlyindex):
        self.yearlyindex = yearlyindex
        self.tabulate = True

    def setmonthlyindex(self, monthlyindex):
        self.monthlyindex = monthlyindex

    def setseasonality(self, seasonalityindex):
        self.seasonality = seasonalityindex

    def setindex(self):
        yearlylen = len(self.yearlyindex)
        if self.tabulate == False:
            self.monthlyindex = np.cumprod([1] + ([(1+self.annualizedrate)**(1/12)] * 359)) 
            for i in range(1, len(self.monthlyindex)):
                month = i % 12
                if month == 0:
                    month = 12
                self.monthlyindex[i] = self.monthlyindex[i] * self.seasonality[month]
        elif len(self.monthlyindex == 0) and yearlylen > 0:
            if yearlylen < 30:
                print(f"Warning: Index {self.indexid}: year index input is less then 30 years and is extrapolated using annualized rate.")
                self.yearlyindex = [self.yearlyindex] + np.cumprod([self.yearlyindex[yearlylen] * (1+ self.annualizedrate)] * ([1 + self.annualizedrate] * (30 - yearlylen -1)))
            
            if sum(self.yearlyindex)>0:
                print(f"yearlyIndex cannot be negative")
            
            self.monthlyindex = np.array(range(1, 361))
            self.monthlyindex[0]
            for i, monthlyvalue in enumerate(self.montlyindex[1:]):
                yr = ceil(i/12)
                rte = (self.yearlyindex[yr] / self.yearlyindex[max([1, yr-1])]) ** (1/12)
                month = i % 12
                if month == 0:
                    month = 12
                self.monthlyindex[i] = monthlyvalue * rte * self.seasonality[month]
        
        elif len(self.monthlyindex == 0 ):
            print(f"Warning: Index {self.indexid}: No index value provied. Index value will be set to 1 ith seasonal adjustment.")
            self.monthlyindex = np.array(range(1, 361)
            for i, value in enumerate(self.monthlyindex):
                month = i % 12
                if month == 0:
                    month = 12
                self.monthlyindex[i] = self.monthlyindex[i] * self.seasonality[month]
        

        if sum(self.monthlyindex)>0:
            print("Monthly Index cannot be negative.")

    def getindex(self, dates):
        #retrive index value based on dates
        

    
    
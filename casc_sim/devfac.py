import numpy as np
from scipy import stats



class devfac(object):

    def __init__(self,indexid, tabulate=False, startdate='2012-01-01', annualizedrate=0):
        self.indexid = indexid
        self.tabulate = False
        self.startdate = startdate
        self.annualizedrate = annualizedrate

        

    def setid(self, value):
        self.facid = value

    def setfacmodel(self, value=False):
        self.facmodel = value

    def setfun(self, value):
        self.fun = value

    def setxname(self, value):
        #returns np.array
        self.xname = value
        self.facmodel = True

    def setparas(self, value):
        #input should be a dict of parameters
        self.paras = value
        self.facmodel = True

    def setmeanlist(self, value):
        '''
        Sets the expected year-to-year loss development factor.
        value should be a np.array
        '''
        self.meanlist = value
        self.facmodel = False

    def setvollist(self, value):
        '''
        Set the year-to-year loss development factor volatility.
        value should be a np.array
        '''
        self.vollist = value
        self.facmodel = False

    def setdevfac(self):
        xnamelen = len(self.xname)
        paraslen = len(self.paras)
        if self.facmodel and (paraslen - xnamelen) != 5:
            print(f"DevFac: {self.indexid}: paras and xname does not match,paras xname does not match. paras contains parameters for variables in the order of Intercept, DevelopmentYear, IncurredLoss, OSRatio ,variables in xname, and Volatility.")
        
        if len(self.meanlist[self.meanlist<0])>0:
            print(f'DevFac {self.indexid}: year to year devement fact in mean list cannot be negative')

        if len(self.vollist[self.vollist < 0 ])>0:
            print(f'Dev Fac {self.indexid}: year to eyar development facrots in vollist cannot be negative')
    



import numpy as np
import time
import pathlib
from collections import namedtuple

class simulation(object):
    def __init__(self, startno, simno, lines, types, workingfolder):
        self.startno = startno
        self.simno = simno
        self.lines=lines
        self.types=types
        classes=("RBNER","ROPEN","IBNR","UPR")
        self.irbnr=True
        self.iROPEN=True
        self.iIBNR=True
        self.iUPR=True
        self.claimobjs=[]
        if len(workingfolder) >0:
            self.workingfolder=pathlib.Path(workingfolder)
        else:
            self.workingfolder.pathlib.Path("./")
        
        self.iCopula=False
		self.freqCopula = "new('CopulaObj',param=c(0,0,0),dimension=3)"
		self.iSummary=True
		self.iReport=True
		self.iFit=True
		self.ncores=1
		self.tag= time.now()
		self.fitfile=""
		self.copfile=""
		self.facfile=""
		self.fitRpt=""
		self.simfile=""
		self.sumfile=""
		self.plog=""
		self.htmlRpt=""
		self.libpath=""


    def claimfitting(self, claimdata, startdate, evaluationdate, linelist, typelist, 
                    discretedist = ["Poisson", "NegativeBinomial", "Geometric"], 
                    continuousdist = ["Normal", "Lognormal", "Pareto", "Weibull", "Gamma", "Uniform","Exponential"], 
                    copulalist = ["Normal"], 
                    reportlag=True, settlementlag=True, frequency=True, severity=True, ssrcorrelation=True, freqcorrelation=True,
                    copulatest=True, totalloss=True, deductible=True, limit=True, check=True ):

        print("fitting process started")
        #from original R file
        if len(claimdata) > 0:
            #some data type conversions
            claimdata[""]

        if (evaluationdate - startdate) < 60 and frequency == True:
            frequency = False
            freqcorrelation=False
            print("Frequency and Frequency Copula Fitting are turned off do to insufficent data")
        #bunch of file name error checking
        if len(self.lines)>0 and len(self.types)>0 and len(self.claimobjs) > 0 and len(claimdata) > 0:
            if self.iFit:
                if self.iReport:
                    fitdir = pathlib.Path(self.workingfolder, 'fit')
                    fitdir.mkdir(exist_ok=True, parents=True)

                

                fitsummary = namedtuple("type", "fit", "distributuion", "method", "parameter", \
                "sd", "p0", "dof", "chisq", "p", "ks", "pks", "loglik", "aic", "bic", "stringsasfactors")
                rfit = 1   
                fitsumcop = namedtuple("lob", "type", "fit", "copula", "method", "parameter", "sd", "dof", "sn", "p", "stringsasfactors")
                rcop = 1
                fitsumfac = namedtuple("lob", "type", "fit", "year", "meanlist", "vollist", "stringsasfactors")
                rfac = 1

                for line in linelist:
                    for claimtype in self.types:
                        fitdata = claimdata[claimdata["lob"]==line & claimdata["type"]==claimtype]
                        obji = 1
                        for co in self.claimobjs:
                            
                            if co.line == line and co.claimtype == claimtype:
                                return
                            obji = obji + 1
                            return

                        if len(fitdata)>5 and co.line == line and co.claimtype == claimtype:
                            if reportlag:
                                f = "reportLag"
                                print(f"Start Fitting Line: {line} Type: {type}  {f}")
                                reportlags = fitdata["reportdate"] - fitdata["occurrencedate"]
                                
                                reportlags = if reportlags == 0, np.random.uniform(), fitdata



import numpy as np
from statsmodels.sandbox.distributions.copula import CopulaBivariate, copula_bv_archimedean, TransfGumbel


class copula(object):

    def __init__(self, type, param, marginal, dimension, dispstr, df, observation, fitmethod, fittest, coutput, fitsucc, info):
        self.type = type
        self.param = param
        self.marginal = marginal
        self.dimension = dimension
        self.dispstr=dispstr
        self.df=df
        self.observation = observation
        self.fitmethod = fitmethod
        self.fittest = fittest
        self.coutput = coutput
        self.fitsucc = fitsucc
        self.into = info


    def setcopulatype(self, value):
        self.type = value

    def setcopluaparam(self, value):
        self.param = value

    def setmarginal(self, value):
        self.marginal = value

    def setdimension(self, value):
        self.dimension = value

    def setdispstr(self, value):
        '''Set parameter matrix format of Elliptical copula.
         value The matrix format. The default is "un" for unstructured. 
         Other choices include "ex" for exchangeable, 
         "ar1" for AR(1), and "toep" for Toeplitz (toeplitz).
        '''
        self.dispstr = value

    def setdf(self, value):
        '''Set the degress of freedom for t copula
        '''
        self.df = value

    def getcopula(self):
        '''gets a copula setup (apparently this is builtinto R)
        '''
        if self.type = "normal" or self.type = "t":
            #ellipcopula
            pass
        else:
            #gumble, frank and clayton
            pass
            




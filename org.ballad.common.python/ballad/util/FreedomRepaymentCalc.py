# encoding: utf-8

'''
Freedom Repayment Calc
Using for calc CHINA 公积金贷款利息
Created on 2015-1-27
@author: BALLAD
'''

class DebayCalc(object):
    '''
    classdocs
    '''
    # Loan interest rate (year)
    ratio = 0.045
    # Total loan amount
    amount = 800000
    # Minimum repayment per month
    min = 4000
    # Maxtium repayment per month
    max = 15000
    # From Minimum to Maxtium
    step = 100
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def calc(self):
        month_ratio = self.ratio / 12 
        for pay in range(self.min, self.max, self.step):
            tatallixi = 0
            amt = self.amount
            months = 0
            while True:
                lixi = amt * month_ratio 
                tatallixi = tatallixi + lixi
                amt = amt + lixi - pay
                months = months + 1
                if (amt <= 0):
                    print (pay, months, tatallixi)
                    break
                
if __name__ == '__main__':
    c = DebayCalc()
    c.calc()

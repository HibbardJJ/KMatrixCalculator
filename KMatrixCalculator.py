# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:37:11 2018

@author: Undergrunt
"""

lbt = 23.12
lat = 23.33
ubt = 23.09
uat = 23.58
R = 255.40

before_average = (lbt+ubt)/2
after_average = (uat+lat)/2



def K_M(rowindex,T_pvalue):
    T_a = ((after_average - before_average)/(rowlength-1))*rowindex + before_average
    return R/(T_pvalue - T_a)



import csv
with open('Snap-KM_23C_1A-000002-001_01_41_18_989.csv','r', encoding='utf-8-sig') as T_pcsvfile, open('K_Matrix_23C_1A.csv','w') as outputfile:
    T_p = csv.reader(T_pcsvfile, delimiter = ',', quotechar='\n')
    while True:
        T_prow=next(T_p)
        rowlength=len(T_prow)
        rowindex=0
        while rowindex < rowlength:
            T_pvalue=float(T_prow[rowindex])
            K_matrix_value = K_M(rowindex,T_pvalue)
            outputfile.write(str(K_matrix_value))
            rowindex+=1
            if rowindex < rowlength:
                outputfile.write(',')
        outputfile.write('\n')

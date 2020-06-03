#!/usr/bin/env python
# coding: utf-8

# In[1]:


def final_depth_integrate(finname,foutname):
    
    #jupyter nbconvert --to script final_depth_integrate.ipynb 
    # Use the above script in a Terminal Window to convert to a .py file

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import statistics as st
    import time as time

    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "last"
    #other options include 'none', 'last', 'last_expr'

    df1=pd.read_csv(finname)  

    df2=df1.copy(deep=True)
    df2.drop(df2[df2[' Layer']!=2].index, inplace=True)
    df2=df2.reset_index(drop=True)
    
    df1=df1.replace([-9999.0, 9999.0, -999.0, 999.0], np.nan)
    df2=df2.replace([-9999.0, 9999.0, -999.0, 999.0], np.nan)
    #df1=df1.replace(9999.0, np.nan)
    #df2=df2.replace(-9999.0, np.nan)
    #df2=df2.replace(9999.0, np.nan)

    df1_interval=np.nanmax(df1[' Interval'])
    df2_interval=np.nanmax(df2[' Interval'])
    mx_interval_int=int(df1_interval)

    #Check that the number or instances with data (# of intervals) equals the number of rows in df2
    if len(np.unique(df1[' Interval'])) != len(df2.index):
        print('Mismatch in Length of Files!!! ' +finname+ ' NOT processed')  
    else:      
        bad_value=-9998
        tic=time.time()
        cnt=0  #Counter is needed in case interval is not sequential in the original csv file
        for i in range (mx_interval_int+1):
            if any(df1[' Interval']==i):
                #print(i)
                loar=df1[' Interval']==i
                #idx=loar[loar==True].index[-1]  #Maybe Not Needed
                #df2[' NASC'][i]=sum((df1[' NASC'])[loar])  #THis Created Warnings!  Better to use iloc like below

                df2.iloc[cnt,df2.columns.get_loc(' Sv_mean')]=bad_value
                df2.iloc[cnt,df2.columns.get_loc(' NASC')]=sum((df1[' NASC'])[loar])

                df2.iloc[cnt,df2.columns.get_loc(' Sv_max')]=np.nanmax((df1[' Sv_max'])[loar])
                df2.iloc[cnt,df2.columns.get_loc(' Sv_min')]=np.nanmin((df1[' Sv_min'])[loar])
                df2.iloc[cnt,df2.columns.get_loc(' Sv_noise')]=bad_value
                df2.iloc[cnt,df2.columns.get_loc(' NASC_noise')]=bad_value

                df2.iloc[cnt,df2.columns.get_loc(' Height_mean')]=sum((df1[' Height_mean'])[loar])
                df2.iloc[cnt,df2.columns.get_loc(' Depth_mean')]=bad_value

                df2.iloc[cnt,df2.columns.get_loc(' Samples')]=sum((df1[' Samples'])[loar])

                df2.iloc[cnt,df2.columns.get_loc(' Layer_depth_max')]=np.nanmax((df1[' Layer_depth_max'])[loar])
                df2.iloc[cnt,df2.columns.get_loc(' Layer_depth_min')]=np.nanmin((df1[' Layer_depth_min'])[loar])

                df2.iloc[cnt,df2.columns.get_loc(' Standard_deviation')]=bad_value
                df2.iloc[cnt,df2.columns.get_loc(' Skewness')]=bad_value
                df2.iloc[cnt,df2.columns.get_loc(' Kurtosis')]=bad_value
                df2.iloc[cnt,df2.columns.get_loc(' ABC')]=sum((df1[' ABC'])[loar])
                df2.iloc[cnt,df2.columns.get_loc(' Area_Backscatter_Strength')]=bad_value

                df2.iloc[cnt,df2.columns.get_loc(' Thickness_mean')]=sum((df1[' Thickness_mean'])[loar])
                df2.iloc[cnt,df2.columns.get_loc(' Range_mean')]=bad_value
                df2.iloc[cnt,df2.columns.get_loc(' Beam_volume_sum')]=sum((df1[' Beam_volume_sum'])[loar])
                cnt=cnt+1
            #tmp_date=df[' Date_M'][loar]
            #f_time.append((df[' Time_M'])[loar])
    toc=time.time()
    elapsed=toc-tic
    #print(elapsed)
    
    df2=df2.fillna(value=-9999.0)
    df2
    df2.to_csv (foutname, index = False, header=True)
    print('Writing ' +foutname+ ' with ' +str(len(df2.index))+ ' rows.') 
    print('Processing took ' +str(elapsed)+ ' seconds.')
    print('')
          
    #import csv
    #csvData=[f_lon, f_lat, f_nasc]

    #zipped=zip(f_date,f_time,f_lon, f_lat, f_nasc)
    #zipped=zip(f_time,f_lon, f_lat, f_nasc)

    #with open('test.csv', 'w') as csvFile:
    #    writer=csv.DictWriter(csvFile, fieldnames=["Time","Lon_M","Lat_M","NASC"])
    #    writer.writeheader()
    #    writer = csv.writer(csvFile)
        #writer.writeheader
    #    writer.writerows(zipped)

    #csvFile.close()

    #type(f_lon)
    


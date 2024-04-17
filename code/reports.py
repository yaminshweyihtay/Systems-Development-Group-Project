import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

FILE_PATH = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])

df = pd.read_csv('Feeding Dashboard data.csv')

numberofrows = len(df)
print("Total patients:")
print(numberofrows)

needsreferral = 0
doesntneedreferral = 0
pip = 0
end_tidal_co2 = 0
feed_vol = 0
oxygen_flow_rate = 0
fio2 = 0
peep = 0
tidal_vol = 0
sip = 0
insp_time = 0


pip2 = []
end_tidal_co22 = []
feed_vol2 = []
oxygen_flow_rate2 = []
fio22 = []
peep2 = []
tidal_vol2 = []
sip2 = []
insp_time2 = []

#checks for missing values in all of the cells of the csv file
na_df = df.isna()

for index, row in df.iterrows():
    value = row['referral']
    if value == 1:
        needsreferral = needsreferral + 1

for index, row in na_df.iterrows():
    if row["pip"] == True :
        pip = pip + 1

for index, row in na_df.iterrows():
    if row["end_tidal_co2"] == True :
        end_tidal_co2 = end_tidal_co2 + 1

for index, row in na_df.iterrows():
    if row["feed_vol"] == True :
        feed_vol = feed_vol + 1

for index, row in na_df.iterrows():
    if row["oxygen_flow_rate"] == True :
        oxygen_flow_rate = oxygen_flow_rate + 1

for index, row in na_df.iterrows():
    if row["fio2"] == True :
        fio2 = fio2 + 1

for index, row in na_df.iterrows():
    if row["peep"] == True :
        peep = peep + 1  

for index, row in na_df.iterrows():
    if row["tidal_vol"] == True :
        tidal_vol = tidal_vol + 1

for index, row in na_df.iterrows():
    if row["sip"] == True :
        sip = sip + 1

for index, row in na_df.iterrows():
    if row["insp_time"] == True :
        insp_time = insp_time + 1

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
for index, row in df.iterrows():
    value = row['pip']
    pip2.append(value)

for index, row in df.iterrows():
    value = row['end_tidal_co2']
    end_tidal_co22.append(value)

for index, row in df.iterrows():
    value = row['feed_vol']
    feed_vol2.append(value)

for index, row in df.iterrows():
    value = row['oxygen_flow_rate']
    oxygen_flow_rate2.append(value)

for index, row in df.iterrows():
    value = row['fio2']
    fio22.append(value)

for index, row in df.iterrows():
    value = row['peep']
    peep2.append(value)

for index, row in df.iterrows():
    value = row['tidal_vol']
    tidal_vol2.append(value)

for index, row in df.iterrows():
    value = row['sip']
    sip2.append(value)

for index, row in df.iterrows():
    value = row['insp_time']
    insp_time2.append(value)

pip3 = np.nanmean(pip2)
end_tidal_co23 = np.nanmean(end_tidal_co22)
feed_vol3 = np.nanmean(feed_vol2)
oxygen_flow_rate3 = np.nanmean(oxygen_flow_rate2)
fio23 = np.nanmean(fio22)
peep3 = np.nanmean(peep2)
tidal_vol3 = np.nanmean(tidal_vol2)
sip3 = np.nanmean(sip2)
insp_time3 = np.nanmean(insp_time2)

print(pip3)
print("avg values:")
avgvalues = [pip3,end_tidal_co23,feed_vol3,oxygen_flow_rate3,fio23,peep3,tidal_vol3,sip3,insp_time3]
print(avgvalues)




missingvalues = [pip,end_tidal_co2,feed_vol,oxygen_flow_rate,fio2,peep,tidal_vol,sip,insp_time]

print(missingvalues)
print("patients in need of referral")
print(needsreferral)








mylabels = ["needs referral: 1601", "doesnt need referral: the rest"] 
mylabels2 = ["pip","end_tidal_co2","feed_vol","oxygen_flow_rate","fio2","peep","tidal_vol","sip","insp_time"]
mydata = [numberofrows,needsreferral]
print(mylabels2)
plt.figure(figsize=(15,6))
plt.pie(mydata,labels=mylabels,autopct='%1.1f%%')
plt.title("Number of patients: 5386")


plt.show()
plt.figure(figsize=(15,6))
plt.bar(mylabels2,missingvalues)
plt.xlabel("columns")
plt.ylabel("number of missing values")
plt.title("Number of missing values")
plt.show()

plt.figure(figsize=(15,6))
plt.bar(mylabels2,avgvalues)
plt.xlabel("columns")
plt.ylabel("average values")
plt.title("average values")
plt.show()



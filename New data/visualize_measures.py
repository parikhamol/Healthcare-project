import sys
import csv
import pandas
from itertools import izip


colnames = ['hospital_name', 'provider_num', 'State', 'measure_name','num_discharges','footnote' ,'excess_readimission','pred_readmission','exp_readmission','num_readmissions','start','end']


data = pandas.read_csv('Hospital_Readmissions_Reduction_Program.csv', names=colnames)

state = data.State.tolist()
num_discharges = data.num_discharges.tolist()
num_readmissions = data.num_readmissions.tolist()
name = data.measure_name.tolist()

measure1_discharges =[]
measure1_readmit =[]
measure2_discharges =[]
measure2_readmit =[]
measure3_discharges =[]
measure3_readmit =[]
measure4_discharges =[]
measure4_readmit =[]
measure5_discharges =[]
measure5_readmit =[]
i =1
while(i<len(state)):
    if num_discharges[i] == "Not Available" :
        if (num_readmissions[i]=="Not Available" or num_readmissions[i] == "Too Few to Report"):
            i=i+1
            continue
        else:
            num_discharges[i] = 0
    if (num_readmissions[i]=="Not Available" or num_readmissions[i] == "Too Few to Report"):
        num_readmissions[i] = 0
    if name[i] == "READM-30-AMI-HRRP":
        measure1_discharges.append(int(num_discharges[i]))
        measure1_readmit.append(int(num_readmissions[i]))
    elif name[i] == "READM-30-COPD-HRRP":
        measure2_discharges.append(int(num_discharges[i]))
        measure2_readmit.append(int(num_readmissions[i]))
    elif name[i] == "READM-30-HF-HRRP":
        measure3_discharges.append(int(num_discharges[i]))
        measure3_readmit.append(int(num_readmissions[i]))
    elif name[i] == "READM-30-HIP-KNEE-HRRP":
        measure4_discharges.append(int(num_discharges[i]))
        measure4_readmit.append(int(num_readmissions[i]))
    elif name[i] == "READM-30-PN-HRRP":
        measure5_discharges.append(int(num_discharges[i]))
        measure5_readmit.append(int(num_readmissions[i]))
    i=i+1


print len(measure1_discharges) + len(measure2_discharges) + len(measure3_discharges) + len(measure4_discharges) +len(measure5_discharges)

measures = ["READM-30-AMI-HRRP","READM-30-COPD-HRRP" ,"READM-30-HF-HRRP","READM-30-HIP-KNEE-HRRP", "READM-30-PN-HRRP"]
avg_discharges = [sum(measure1_discharges)/float(len(measure1_discharges)),sum(measure2_discharges)/float(len(measure2_discharges)),sum(measure3_discharges)/float(len(measure3_discharges)),sum(measure4_discharges)/float(len(measure4_discharges)),sum(measure5_discharges)/float(len(measure5_discharges))]

avg_readmission = [sum(measure1_readmit)/float(len(measure1_readmit)),sum(measure2_readmit)/float(len(measure2_readmit)),sum(measure3_readmit)/float(len(measure3_readmit)),sum(measure4_readmit)/float(len(measure4_readmit)),sum(measure5_readmit)/float(len(measure5_readmit))]

ratio =[]
for i in range(len(avg_discharges)):
    ratio.append(float(avg_readmission[i])*100/avg_discharges[i])

with open("measure_wise_discharge_readmissions.csv","w") as f:
    writer=csv.writer(f)
    writer.writerows(izip(measures, avg_discharges, avg_readmission,ratio))



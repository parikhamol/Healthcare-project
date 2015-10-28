import sys
import csv
import pandas
from itertools import izip


colnames = ['hospital_name', 'provider_num', 'State', 'measure_name','num_discharges','footnote' ,'excess_readimission','pred_readmission','exp_readmission','num_readmissions','start','end']


data = pandas.read_csv('Hospital_Readmissions_Reduction_Program.csv', names=colnames)

state = data.State.tolist()
num_discharges = data.num_discharges.tolist()
num_readmissions = data.num_readmissions.tolist()

avg_discharges =[]
state_arr =[]
temp = state [1]
i=1
sum_discharges =0
num_hos = 0
while(i<len(state)):
    if state[i] == temp:
        if num_discharges[i] == 'Not Available':
            num_discharges[i] = 0
            num_hos = num_hos - 1
        sum_discharges = sum_discharges + int(num_discharges[i])
        i = i +1
        num_hos = num_hos + 1
        continue
    else:
        avg_discharges.append(sum_discharges/float(num_hos) )
        state_arr.append(temp)
        temp = state[i]
        if num_discharges[i] == 'Not Available':
            num_discharges[i] = 0
        sum_discharges = int(num_discharges[i])
        i = i+1
        num_hos =1

state_arr.append(temp)
avg_discharges.append(sum_discharges/float((num_hos-1)))


i=1
avg_readmissions =[]
num_hos = 0
sum_readmissions = 0
temp =state[1]

while(i<len(state)):
    if state[i] == temp:
        if num_readmissions[i] == 'Too Few to Report' or num_readmissions[i] == 'Not Available':
            num_readmissions[i] = 0
            num_hos = num_hos - 1
        sum_readmissions = sum_readmissions + int(num_readmissions[i])
        i = i +1
        num_hos = num_hos + 1
        continue
    else:
        avg_readmissions.append(sum_readmissions/float(num_hos))
        temp = state[i]
        if num_readmissions[i] == 'Too Few to Report' or num_readmissions[i] == 'Not Available':
            num_readmissions[i] = 0
        sum_readmissions = int(num_readmissions[i])
        i = i+1
        num_hos =1


avg_readmissions.append(sum_readmissions/float((num_hos-1)))


ratio =[]

for i in range(len(avg_readmissions)):
    ratio.append(avg_readmissions[i]*100/avg_discharges[i])

print ratio
with open("state_wise_discharge_readmissions.csv", "w") as f:
    writer=csv.writer(f)
    writer.writerows(izip(state_arr,avg_discharges,avg_readmissions, ratio))






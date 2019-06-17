'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

censusdata = pd.read_csv('cleaned_dataset.csv')

# 1. income < and > 50k
income = censusdata['Income'].value_counts()
inclessthan50 = income['<=50K']
incgreaterthan50 = income['>50K']
y = [inclessthan50,incgreaterthan50]
n = len(y)
x = range(n)
width = 0.3
plt.xticks(x,('less than 50K','more than 50K'))
plt.xlabel('Income')
plt.ylabel('number of people')
plt.title('Count of the two possible outcome variables')
#plt.bar(x,y,width)
#plt.show()

#2 agw range with income
lessthan20 = censusdata[(censusdata.Age > 0) & (censusdata.Age <= 20)]
income1 = lessthan20['Income'].value_counts()
income1less = income1['<=50K']
income1greater = income1['>50K']

lessthan30 = censusdata[(censusdata.Age > 20) & (censusdata.Age <= 30)]
income2 = lessthan30['Income'].value_counts()
income2less = income2['<=50K']
income2greater = income2['>50K']

lessthan40 = censusdata[(censusdata.Age > 30) & (censusdata.Age <= 40)]
income3 = lessthan40['Income'].value_counts()
income3less = income3['<=50K']
income3greater = income3['>50K']

lessthan50 = censusdata[(censusdata.Age > 40) & (censusdata.Age <= 50)]
income4 = lessthan50['Income'].value_counts()
income4less = income4['<=50K']
income4greater = income4['>50K']

lessthan60 = censusdata[(censusdata.Age > 50) & (censusdata.Age <= 60)]
income5 = lessthan60['Income'].value_counts()
income5less = income5['<=50K']
income5greater = income5['>50K']

lessthan70 = censusdata[(censusdata.Age > 60) & (censusdata.Age <= 70)]
income6 = lessthan70['Income'].value_counts()
income6less = income6['<=50K']
income6greater = income6['>50K']

lessthan80 = censusdata[(censusdata.Age > 70) & (censusdata.Age <= 80)]
income7 = lessthan80['Income'].value_counts()
income7less = income7['<=50K']
income7greater = income7['>50K']

lessthan90 = censusdata[(censusdata.Age > 80) & (censusdata.Age <= 90)]
income8 = lessthan90['Income'].value_counts()
income8less = income8['<=50K']
income8greater = income8['>50K']

lessthangroup1 = [income1less,income2less,income3less,income4less,income5less,income6less,income7less,income8less]
greaterthangroup1 = [income1greater,income2greater,income3greater,income4greater,income5greater,income6greater,income7greater,income8greater]

n = 8
xaxis = range(n)
#p1 = plt.bar(xaxis, lessthangroup1, width)
#p2 = plt.bar(xaxis, greaterthangroup1, width,bottom=lessthangroup1)

plt.ylabel('Age count')
plt.xlabel('Age groups')
plt.title('Income with respect to age groups')
plt.xticks(xaxis, ('0-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90'))
#plt.legend((p1, p2), ('less than 50K', 'more than 50K'))

#plt.show()

#3. Income with respect to sex
lessthan = censusdata[censusdata.Income == '<=50K']
count1 = lessthan['Sex'].value_counts()
maleless = count1['Male']
femaleless = count1['Female']

morethan = censusdata[censusdata.Income == '>50K']
count2 = morethan['Sex'].value_counts()
malemore = count2['Male']
femalemore = count2['Female']

lessthangroup2 = [maleless,femaleless]
greaterthangroup2 = [malemore,femalemore]

n = 2
xaxis1 = range(n)
#p11 = plt.bar(xaxis1, lessthangroup2, width)
#p22 = plt.bar(xaxis1, greaterthangroup2, width,bottom=lessthangroup2)

plt.ylabel('Sex count')
plt.xlabel('Sex groups')
plt.title('Income with respect to sex groups')
plt.xticks(xaxis, ('Male', 'Female'))
#plt.legend((p11, p22), ('less than 50K', 'more than 50K'))

#plt.show()

#4. worker groups and income
lessthan = censusdata[censusdata.Income == '<=50K']
count3 = lessthan['Workclass'].value_counts()
private = count3['Private']
selfemp = count3['Self-emp-not-inc']
locgov = count3['Local-gov']
stategov = count3['State-gov']
fedgov = count3['Federal-gov']
selfempinc = count3['Self-emp-inc']

morethan = censusdata[censusdata.Income == '>50K']
count4 = morethan['Workclass'].value_counts()
private1 = count4['Private']
selfemp1 = count4['Self-emp-not-inc']
locgov1 = count4['Local-gov']
stategov1 = count4['State-gov']
fedgov1 = count4['Federal-gov']
selfempinc1 = count4['Self-emp-inc']

lessthangroup3 = [private,selfemp,locgov,stategov,fedgov,selfempinc]
greaterthangroup3 = [private1,selfemp1,locgov1,stategov1,fedgov1,selfempinc1]

n = 6
xaxis2 = range(n)
#p111 = plt.bar(xaxis2, lessthangroup3, width)
#p222 = plt.bar(xaxis2, greaterthangroup3, width,bottom=lessthangroup3)

plt.ylabel('workers count')
plt.xlabel('Worker groups')
plt.title('Income with respect to worker groups')
plt.xticks(xaxis2, ('private', 'self employed not inc','local governament','state governament','fedral governament','self employed inc'))
#plt.legend((p111, p222), ('less than 50K', 'more than 50K'))

#plt.show()

#5. Income with education
lessthan = censusdata[censusdata.Income == '<=50K']
count5 = lessthan['Education'].value_counts()
hs = count5['HS-grad']
college = count5['Some-college']
bach = count5['Bachelors']
assoc = count5['Assoc-voc']
eleven = count5['11th']
assoc2 = count5['Assoc-acdm']
ten = count5['10th']
masters = count5['Masters']
eight = count5['7th-8th']
nine = count5['9th']
twelve = count5['12th']
prof = count5['Prof-school']
five = count5['5th-6th']
doc = count5['Doctorate']
one = count5['1st-4th']

morethan = censusdata[censusdata.Income == '>50K']
count6 = morethan['Education'].value_counts()
hs1 = count6['HS-grad']
college1 = count6['Some-college']
bach1 = count6['Bachelors']
assoc11 = count6['Assoc-voc']
eleven1 = count6['11th']
assoc22 = count6['Assoc-acdm']
ten1 = count6['10th']
masters1 = count6['Masters']
eight1 = count6['7th-8th']
nine1 = count6['9th']
twelve1 = count6['12th']
prof1 = count6['Prof-school']
five1 = count6['5th-6th']
doc1 = count6['Doctorate']
one1 = count6['1st-4th']

lessthangroup4 = [hs,college,bach,assoc,eleven,assoc2,ten,masters,eight,nine,twelve,prof,five,doc,one]
greaterthangroup4 = [hs1,college1,bach1,assoc11,eleven1,assoc22,ten1,masters1,eight1,nine1,twelve1,prof1,five1,doc1,one1]

n = 15
xaxis3 = range(n)
#p1111 = plt.bar(xaxis3, lessthangroup4, width)
#p2222 = plt.bar(xaxis3, greaterthangroup4, width,bottom=lessthangroup4)

plt.ylabel('people count')
plt.xlabel('education groups')
plt.title('Income with respect to education groups')
#plt.xticks(xaxis3, ('high school','college','bachelors','assoc-voc','11th','assoc-acdm','10th','Masters','7th-8th','9th','12th','Prof-school','5th-6th','Doctrate','1st-4th','Preschool'))
#plt.legend((p1111, p2222), ('less than 50K', 'more than 50K'))

#plt.show()

#6 maritial status with income

lessthan = censusdata[censusdata.Income == '<=50K']
count7 = lessthan['Marital_Status'].value_counts()
nm = count7['Never-married']
mcs = count7['Married-civ-spouse']
div = count7['Divorced']
sep = count7['Separated']
wid = count7['Widowed']
msa = count7['Married-spouse-absent']

morethan = censusdata[censusdata.Income == '>50K']
count8 = morethan['Marital_Status'].value_counts()
nm1 = count8['Never-married']
mcs1 = count8['Married-civ-spouse']
div1 = count8['Divorced']
sep1 = count8['Separated']
wid1 = count8['Widowed']
msa1 = count8['Married-spouse-absent']

lessthangroup5 = [nm,mcs,div,sep,wid,msa]
greaterthangroup5 = [nm1,mcs1,div1,sep1,wid1,msa1]

n = 6
xaxis4 = range(n)
width5 = 0.4
#p11111 = plt.bar(xaxis4, lessthangroup5, width5)
#p22222 = plt.bar(xaxis4, greaterthangroup5, width5,bottom=lessthangroup5)

plt.ylabel('people count')
plt.xlabel('maritial status')
plt.title('Income with respect to martial status')
labels = ['never married','married-civ-spouse','Divorced','Seperated','Widowed','married-spouse-absent']
plt.xticks(xaxis3, labels, rotation='vertical')
#plt.margins(0.2)
#plt.subplots_adjust(bottom=0.4)
#plt.legend((p11111, p22222), ('less than 50K', 'more than 50K'))

#plt.show()

'''
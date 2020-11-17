HighestTransport=30
NameList=['Tom','Patric','Russel','Steven','Kevin','Frank','Alice','Louis','Rose','Lily']
name=input("Please tell us your name:")
if name=='Tom':
    Transport=[30,10,30,30,30,25,25,30,30,15]
if name=='Patrick':
    Transport=[25,10,30,30,20,20,30,20,30,25]
if name=='Russel':
    Transport=[30,15,30,30,30,25,30,25,30,25]
if name=='Steven':
    Transport=[30,15,30,30,30,25,25,30,30,15]
if name=='Kevin':
    Transport=[30,20,30,30,30,25,30,20,30,20]
if name=='Frank':
    Transport=[30,20,30,30,25,30,30,30,25,30]
if name=='Alice':
    Transport=[30,10,30,30,30,20,25,30,30,10]
if name=='Louis':
    Transport=[30,20,30,30,30,25,30,25,30,25]
if name=='Rose':
    Transport=[25,20,30,30,25,30,30,25,30,20]
if name=='Lily':
    Transport=[25,15,30,30,25,30,30,25,30,20]
HighestScore=30


Name=["Waiter","Construction Worker","Private tutor","Programming intership",
      "Hand out leaflets","Cleaning","Dishwasher",
      "Cashier","Libririan","Warehouse Administration"]
STpoint=float(input("please input weight on starting time; "))
ETpoint=float(input("please input weight on ending time; "))
TimeLengthpoint=float(input("please input weight on working length; "))
Transpoint=float(input("Please input your weight on transportation method: ")) 
Physicalpoint=float(input("please input weight on physical work; "))
Mentalpoint=float(input("please input weight on brain work; "))
Environmentpoint=float(input("please input weight on environment; "))
Wagepoint=float(input("please input weight on wage; "))
TTimepoint=float(input("please input weight on transport time ; "))
SelfActualPoint=float(input("please input weight on self actualisation; "))
SocialPoint=float(input("please input weight on social activities; "))
Safety=float(input("please input weight on safety; "))
TotalPoint=STpoint+ETpoint+TimeLengthpoint+Physicalpoint+Mentalpoint+Environmentpoint+Wagepoint+TTimepoint+SelfActualPoint+SocialPoint+Safety
print("the total is: ")
print(TotalPoint)
FinalResultST=[]
FinalResultET=[]
FinalResultL=[]
FinalResultTrans=[]
FinalResultPhysical=[]
FinalResultMental=[]
FinalResultEnvironment=[]
FinalResultWage=[]
FinalResultTime=[]
FinalResultActual=[]
FinalResultSocial=[]
FinalResultSafety=[]
FinalFinal=[]



#start time
personStart=float(input("Please input the personal expectation for starting time: "))
ArrayOfST=[9,8,8,9,9,9,8,10,10,6]#change
max1=-10000#change if
for counter in range(0,10,1):
    if ArrayOfST[counter]>max1:#change if
        max1=ArrayOfST[counter]#change
for counter2 in range(0,10,1):
    if personStart!=max1:#change if 
        result=((personStart-ArrayOfST[counter2])/(personStart-max1))#change
        final=result*(STpoint/TotalPoint)#change
        FinalResultST.append(final)
    elif ArrayOfST[counter2]==max1:
         FinalResultST.append(0)
    elif ArrayOfST[counter2]!=max1:
        k=0-ArrayOfST[counter2]
        FinalResultST.append((k)*(STpoint/TotalPoint))
    

#for i in range(0,10,1):
 #   print(FinalResultST[i])
#end time   
personEnd=float(input("Please input the personal expectation for ending time: "))
ArrayOfET=[8,6,4,5,6,6,6,8,4,7]#change--
min1=10000#change if--
for counter in range(0,10,1):
    if ArrayOfET[counter]<min1:#change if
        min1=ArrayOfET[counter]#change
for counter2 in range(0,10,1):
    if personEnd!=min1:#change --
        result=((personEnd-ArrayOfET[counter2])/(personEnd-min1))#change--
        final=result*(ETpoint/TotalPoint)#change--
        FinalResultET.append(final)
    elif ArrayOfET[counter2]==min1:
         FinalResultET.append(0)
    elif ArrayOfET[counter2]!=min1:
        k=0-ArrayOfET[counter2]
        FinalResultET.append((k)*(ETpoint/TotalPoint))
        
#time length
personLength=float(input("Please input the personal expectation for working time length: "))
ArrayOfL=[11,10,8,8,9,9,10,10,6,13]#change--
min2=-10000#change if--
for counter in range(0,10,1):
    if ArrayOfL[counter]<min2:#change if--
        min2=ArrayOfL[counter]#change--
for counter2 in range(0,10,1):
    if personLength!=min2:#change if --
        result=((personLength-ArrayOfL[counter2])/(personLength-min2))#change--
        final=result*(TimeLengthpoint/TotalPoint)#change--
        FinalResultL.append(final)
    elif ArrayOfL[counter2]==min2:
         FinalResultL.append(0)
    elif ArrayOfL[counter2]!=min2:
        k=0-ArrayOfL[counter2]
        FinalResultL.append((k)*(TimeLengthpoint/TotalPoint))
   
#Transport Method
for counter in range(0,5,1):
    print("please input the No,",counter+1)
    Method=input("transportation method you prefer: ")
for counter in range(0,10,1):
    FinalResultTrans.append((Transport[counter]/30)*(Transpoint/TotalPoint))   
    

#final physical
personPhysical=float(input("Please input the personal expectation for physical output: "))
ArrayOfP=[6,10,4,2,8,9,6,5,3,10]#change--
min3=10000#change if--
for counter in range(0,10,1):
    if ArrayOfP[counter]<min3:#change if
        min3=ArrayOfP[counter]#change
for counter2 in range(0,10,1):
    if personPhysical!=min3:#change --
        result=((personPhysical-ArrayOfP[counter2])/(personPhysical-min3))#change--
        final=result*(Physicalpoint/TotalPoint)#change--
        FinalResultPhysical.append(final)
    elif ArrayOfP[counter2]==min3:
         FinalResultET.append(0)
    elif ArrayOfP[counter2]!=min3:
        k=0-ArrayOfP[counter2]
        FinalResultPhysical.append((k)*(Physicalpoint/TotalPoint))
    

#mental
personMental=float(input("Please input the personal expectation for mental output: "))
ArrayOfM=[3,1,9,10,2,1,1,4,7,2]#change--
min4=10000#change if--
for counter in range(0,10,1):
    if ArrayOfM[counter]<min4:#change if
        min4=ArrayOfM[counter]#change
for counter2 in range(0,10,1):
    if personMental!=min4:#change --
        result=((personMental-ArrayOfM[counter2])/(personMental-min4))#change--
        final=result*(Mentalpoint/TotalPoint)#change--
        FinalResultMental.append(final)
    elif ArrayOfM[counter2]==min4:
         FinalResultMental.append(0)
    elif ArrayOfM[counter2]!=min4:
        k=0-ArrayOfM[counter2]
        FinalResultMental.append((k)*(Mentalpoint/TotalPoint))
    
    

#environment
personE=float(input("Please input the personal expectation for the environment: "))
ArrayOfE=[8,3,10,10,4,3,3,7,9,5]#change
max2=-10000#change if
for counter in range(0,10,1):
    if ArrayOfE[counter]>max2:#change if
        max2=ArrayOfE[counter]#change
for counter2 in range(0,10,1):
    if personE!=max2:#change if 
        result=((personE-ArrayOfE[counter2])/(personE-max2))#change
        final=result*(Environmentpoint/TotalPoint)#change
        FinalResultEnvironment.append(final)
    elif ArrayOfE[counter2]==max2:
         FinalResultEnvironment.append(0)
    elif ArrayOfE[counter2]!=max2:
        k=0-ArrayOfE[counter2]
        FinalResultEnvironment.append((k)*(Environmentpoint/TotalPoint))

#Wage
personW=float(input("Please input the personal expectation for the wage: "))
ArrayOfW=[30,30,40,50,25,28,16,18,35,28]#change
max3=-10000#change if
for counter in range(0,10,1):
    if ArrayOfW[counter]>max3:#change if
        max3=ArrayOfW[counter]#change
for counter2 in range(0,10,1):
    if personW!=max3:#change if 
        result=((personW-ArrayOfW[counter2])/(personW-max3))#change
        final=result*(Wagepoint/TotalPoint)#change
        FinalResultWage.append(final)
    elif ArrayOfW[counter2]==max3:
         FinalResultWage.append(0)
    elif ArrayOfW[counter2]!=max3:
        k=0-ArrayOfW[counter2]
        FinalResultWage.append((k)*(Wagepoint/TotalPoint))

    

#time transport
#end time   
personT=float(input("Please input the personal expectation for the time spent on transport: "))
ArrayOfT=[0.5,1.5,1,0,1.5,0.3,2,0.5,1,0.2]#change--
min5=10000#change if--
for counter in range(0,10,1):
    if ArrayOfT[counter]<min5:#change if
        min5=ArrayOfT[counter]#change
for counter2 in range(0,10,1):
    if personT!=min1:#change --
        result=((personT-ArrayOfT[counter2])/(personT-min5))#change--
        final=result*(TTimepoint/TotalPoint)#change--
        FinalResultTime.append(final)
    elif ArrayOfT[counter2]==min5:
         FinalResultTime.append(0)
    elif ArrayOfT[counter2]!=min5:
        k=0-ArrayOfT[counter2]
        FinalResultTime.append((k)*(TTimepoint/TotalPoint))


#Self-actualization
personA=float(input("Please input the personal expectation on the Self-actualization level: "))
ArrayOfA=[1,1,9,10,3,4,4,4,8,2]#change
max4=-10000#change if
for counter in range(0,10,1):
    if ArrayOfA[counter]>max4:#change if
        max4=ArrayOfA[counter]#change
for counter2 in range(0,10,1):
    if personA!=max4:#change if 
        result=((personA-ArrayOfA[counter2])/(personA-max4))#change
        final=result*(SelfActualPoint/TotalPoint)#change
        FinalResultActual.append(final)
    elif ArrayOfA[counter2]==max4:
         FinalResultActual.append(0)
    elif ArrayOfA[counter2]!=max4:
        k=0-ArrayOfA[counter2]
        FinalResultActual.append((k)*(SelfActualPoint/TotalPoint))

    
#Social
personO=float(input("Please input the personal expectation on the Social needs: "))
ArrayOfO=[7,4,10,3,5,6,7,6,9,2]#change
max5=-10000#change if
for counter in range(0,10,1):
    if ArrayOfO[counter]>max5:#change if
        max5=ArrayOfO[counter]#change
for counter2 in range(0,10,1):
    if personO!=max5:#change if 
        result=((personO-ArrayOfO[counter2])/(personO-max5))#change
        final=result*(SocialPoint/TotalPoint)#change
        FinalResultSocial.append(final)
    elif ArrayOfO[counter2]==max5:
         FinalResultSocial.append(0)
    elif ArrayOfO[counter2]!=max5:
        k=0-ArrayOfO[counter2]
        FinalResultSocial.append((k)*(SocialPoint/TotalPoint))

   

#Safety
personS=float(input("Please input the personal expectation on safety: "))
ArrayOfS=[10,4,10,8,3,8,9,9,9,7]#change
max6=-10000#change if
for counter in range(0,10,1):
    if ArrayOfS[counter]>max6:#change if
        max6=ArrayOfS[counter]#change
for counter2 in range(0,10,1):
    if personS!=max6:#change if 
        result=((personS-ArrayOfS[counter2])/(personS-max6))#change
        final=result*(Safety/TotalPoint)#change
        FinalResultSafety.append(final)
    elif ArrayOfS[counter2]==max6:
         FinalResultSafety.append(0)
    elif ArrayOfS[counter2]!=max6:
        k=0-ArrayOfS[counter2]
        FinalResultSafety.append((k)*(Safety/TotalPoint))

for counter3 in range(0,10,1):
    FinalFinal.append(FinalResultST[counter3]+FinalResultET[counter3]+FinalResultL[counter3]+FinalResultTrans[counter3]+FinalResultPhysical[counter3]+FinalResultMental[counter3]+FinalResultEnvironment[counter3]+FinalResultWage[counter3]+FinalResultTime[counter3]+FinalResultActual[counter3]+FinalResultSocial[counter3]+FinalResultSafety[counter3])
    print("Score for the job")
    print(Name[counter3]+'is')
    print(FinalFinal[counter3])
MAX=-10000000
for counter4 in range(0,10,1):
    if FinalFinal[counter4]>MAX:
        MAX=FinalFinal[counter4]
        Position=counter4
print("The job with highest score: ")
print(FinalFinal[Position]) 
print(Name[Position])

import csv 
import numpy as np

file = open("Sampledata3.csv", "r")
obj = csv.reader(file)
aa = []

for i in obj:
    aa.append(i)


class analysis:
    def __init__(self,data):
        self.data=data
        self.length=len(self.data)

    def Doubletop(self):
        #print(tp)
        ask=0
        lst=[]
        fin_lst=[]
        dac=[subseq[4] for subseq in self.data]
        

 # if i>=len(self.data)-20:
                #    break
        for i in range(1,10000,70):
            if i>=len(self.data)-70:
                    break
            
            for kk in range(i,i+65):
                start=kk
                end=kk+20
                mid=(start+end)//2
                
                #print(start,"$$$",end)
                strt_time=kk
                peak1=max(dac[start:mid])
                peak2=max(dac[mid:end])
                in1=int(dac.index(peak1))
                in2=int(dac.index(peak2))
                low=min(dac[in1:in2])
                low_ind=int(dac.index(low))
                a=abs(in1-in2)
                count=0
                dist1=in1-start
                dist2=end-in2
                if dac[in1]>dac[start] and dac[in2]>dac[end] and dist1>2 and dist2>3 and  a<=10:
                    
                    
                    if (((in1-start)<5 and ((in1-start)>=2) and (end-in2)<=9)) and abs(float(peak1)-float(peak2))<101:
                        
                        strt_ind=start
                        End_time=end
                        for m in range(start,in1+1):
                            if (float(self.data[m][3])<float(self.data[m+1][3])):
                                pass
                            else:
                                strt_time=m
                                break
                        for down in range(in2,end):
                            if (float(self.data[down][1])>float(self.data[down+1][2])):
                                pass
                            else:
                                End_time=down
                                break
                        
                        if (End_time-strt_time)<20 and (End_time-strt_time)>10 :
                            lst.append(['',self.data[strt_time][5],self.data[End_time][5],"Double Top"])
        return lst                 
"""  #print(in1,"&&",in2)
                    strt_time=i
                    End_time=i+20
                    for m in range(in1,start,-1):
                        if (float(self.data[m][1])<float(self.data[m][2])) or (float(self.data[m][1])-float(self.data[m][2])<1):# or dac[m]>dac[m+1]:
                            pass
                        else:
                            
                            strt_time=m

                            break
                    for down in range(in2,end):
                        if (float(self.data[down][1])>float(self.data[down][2])) or(float(self.data[down][1])-float(self.data[down][2])<1):# or dac[m]<dac[m+1]:
                            pass
                        else:
                            End_time=down
                            break
                    #for check in range(in1,low_ind):
                     #   if dac

                    
                        
                    
                    #print(in1-start)
                    if (((in1-start)<4 and ((in1-start)>=2) and (end-in2)<=9)) and (End_time-strt_time<80 and End_time-strt_time>50) :
                        #print(i)#((in1-i)<5) and (dac[div]==low)
                        #print(["start:-",self.data[strt_time][5],"end:-",self.data[End_time][5]])
                        lst.append([0,self.data[strt_time][5],self.data[End_time][5],"Double Top"])
                    else:
                        pass 
                    
                    #print(in1,"$",i)
                    #print(in1-i)
                    #print(abs((in2-(i+25))))
                    #print((abs((in2-(i+25))<=12)) and (abs((in2-(i+25))>5)))
                    
                else:
"""                       
                        #print(["start:-",self.data[in1-2][5],"end:-",self.data[in2+5][5]])
                        #lst.append(["start:-",self.data[in1-2][5],"end:-",self.data[in2+5][5]])
"""          for m in lst:
            if m in fin_lst:
                pass
            else:
                fin_lst.append(m)
        return fin_lst
"""   

            
 





class analysis:
    def __init__(self,data):
        self.data=data
        self.length=len(self.data)

    def Doubletop(self):
        #print(tp)
        ask=0
        lst=[]
        fin_lst=[]
        dac=[]
        for subseq in self.data:
            if subseq[4]=="high":
                pass
            else:
                dac.append(float(subseq[4]))
        #dac=[float(subseq[4]) for subseq in self.data]
        

 # if i>=len(self.data)-20:
                #    break
        for i in range(5,10000,70):
            if i>=len(self.data)-70:
                    break
        for kk in range(i,i+65):
            try:
                start=kk
                end=kk+25
                mid=(start+end)//2
                peak1=max(dac[start:end])
                peak1_ind=int(dac.index(peak1))
                right_shoulder=max(dac[start:peak1_ind])
                left_shoulder=max(dac[peak1_ind:end])
                right_should_ind=int(dac.index(right_shoulder))
                low_right_side=min(dac[start:peak1_ind])
                low_left_side=min(dac[peak1_ind:end])
                left_should_ind=int(dac.index(left_shoulder))
                strt_time=kk
                end_time=kk+25
                low_right_ind=int(dac.index(low_right_side))
                low_left_ind=int(dac.index(low_left_side))
                lst=[]
                fin_lst=[]
                if abs(left_shoulder-right_shoulder)<0.5 and (low_right_side<right_shoulder) and(low_left_side<left_shoulder)and (peak1>right_shoulder and peak1>left_shoulder) :
                    for m in range(start,right_should_ind+1):
                        if (float(self.data[m][3])<float(self.data[m+1][3])):
                            pass
                        else:
                        
                            break
                    for m in range(right_should_ind,low_right_ind):
                        if (float(self.data[m][3])>float(self.data[m+1][3])):
                            pass
                        else:
                            break
                    for m in range(low_right_ind,peak1_ind):
                         if (float(self.data[m][3])<float(self.data[m+1][3])):
                             pass
                         else:
                             break
                    for m in range(peak1_ind,low_left_ind):
                        if (float(self.data[m][3])>float(self.data[m+1][3])):
                                pass
                        else:
                        
                            break
                    for m in range(low_left_ind,left_should_ind):
                        if (float(self.data[m][3])<float(self.data[m+1][3])):
                                pass
                        else:
                        

                            break
                    for m in range(left_should_ind,end):
                        if (float(self.data[m][3])>float(self.data[m+1][3])):
                                pass
                        else:

                            break
                    
                    lst.append(["",self.data[strt_time],self.data[end_time],"Head and shoulders"])
            except:
                pass
            for m in lst:
                if m in fin_lst:
                    pass
                else:
                    fin_lst.append(m)
        return fin_lst 
                
                
       
 



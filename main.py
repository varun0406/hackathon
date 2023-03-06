import csv
import doubletop
import doublebottom
import headandshoulders


ask=input("enter file name to read from and keep it in same directory")
file = open(ask+".csv", "r")
obj = csv.reader(file)
aa = []

for i in obj:
    aa.append(i)
db=doublebottom.analysis(aa)
lst=db.Doublebottom()
dt=doubletop.analysis(aa)
lst1=dt.Doubletop()
has=headandshoulders.analysis(aa)
lst2=has.Doubletop()
final_lst=[]
for i in lst:
    final_lst.append(i)
for i in lst1:
    final_lst.append(i)
fif_list=[]
for m in final_lst:
    if m in fif_list:
        pass
    else:
        fif_list.append(m)
fif_list.sort()


with open(ask+"GT.csv","w")  as filee:
    obj=csv.writer(filee)
    obj.writerow(['','start','end','pattern'])
    obj.writerows(fif_list)






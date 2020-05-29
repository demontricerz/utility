t=open(input('Enter the input file name: '))
y=open(input('Enter the output file name: '),"w")
y.write(r"<table cellpadding='15' align='center' border='1px solid black' width='100%'>")
y.write(r"<tr align='center'><td><b>S.No</b></td><td><b>Name</b></td><td><b>Mobile Number</b></td></tr>")
cou=1
for line in t.readlines():
    m=line[:]
    m=f"<tr align='center'><td >{cou}</td><td>"+m
    m=m.replace('\t',r"</td><td><a href='tel: ")
    m=m.replace('\n',r"'> click here to call </a></td></tr>")
    y.write(m)
    cou+=1
y.write(r"</table>")
t.close()
y.close()

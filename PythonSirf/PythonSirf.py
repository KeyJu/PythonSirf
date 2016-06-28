#coding:utf-8
 
filename = ['sirf 001.gps','sirf 002.gps']
name = ['Satellite ID','GPS Time','Pseudorange','Carrier Phase','C/N']
i = 1 
for fn in filename:
    fr = open(fn,'r')
    fw = open('sirf%d.txt' % i,  'w')  
    buffer = []
    print(name[0].rjust(15)+name[1].rjust(18)+name[2].rjust(20)+name[3].rjust(20)+name[4].rjust(10))
    fw.write(name[0].rjust(15)+name[1].rjust(18)+name[2].rjust(20)+name[3].rjust(20)+name[4].rjust(10))
    fw.write("\n")        
    for line in open(fn):  
        line = fr.readline
        buffer = line.split(',')
        if buffer[0] == '28':
            need = [] 
            need.append(buffer[3])
            need.append( ("%0.3f" % float(buffer[4])))
            need.append( ("%0.3f" % float(buffer[5])))
            need.append( ("%0.3f" % float(buffer[7])))
            need.append( buffer[10])                      
            print(need[0].rjust(15)+need[1].rjust(18)+need[2].rjust(20)+need[3].rjust(20)+need[4].rjust(10))
            fw.write(need[0].rjust(15)+need[1].rjust(18)+need[2].rjust(20)+need[3].rjust(20)+need[4].rjust(10))
            fw.write("\n")  
    i = i+1
    fr.close()
    fw.close()    

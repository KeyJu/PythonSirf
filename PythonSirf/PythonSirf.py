#coding:utf-8
  
filename = ['sirf 001.gps','sirf 002.gps']
i = 1 
for fn in filename:
    fr = open(fn,'r')
    fw = open('sirf%d.txt' % i,  'w')  
    buffer = []  

    for line in open(fn):  
        line = fr.readline() 
        buffer = line.split(',')
        if buffer[0] == '28':
            need = [] 
            need.append( buffer[0])
            need.append( buffer[1])
            need.append( buffer[2])
            need.append( ("%0.3f" % float(buffer[7])))
            need.append( buffer[10])        
            print (need)
            fw.write(str(need))
            fw.write("\n")   
    i = i+1
    fr.close()
    fw.close()    

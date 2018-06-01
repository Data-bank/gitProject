# Daybreaker's UTF-8 Converter in Python
# distributed by GNU Public License
import os, re, traceback
count_success = 0; count_failed = 0

def convfile(path):
     data = open(path,'r').read().decode('cp949')
     open(path,'w').write(data.encode('utf8'))

def convdir(path):
    global count_success, count_failed
    entrylist = os.listdir(path)
    for x in entrylist:
        if os.path.isdir(x):
            convdir(path + "/" + x)
        else:
            m = re.search("\.([^.]+)$",x)
            if(m is not None):
                ext = m.group(0).lstrip('.')
                if ext in ('php','php3','htm','html','txt','css','js','sql'):
                    try:
                        convfile(path+"/"+x)
                        print path+"/"+x
                        count_success+=1
                    except:
                        print "** Error on processing "+path+"/"+ x
                        traceback.print_exc()
                        count_failed+=1
                else:
                    pass
            # if you want convert files which don't have extensions, decomment the next line.
            #else convfile(path+"/"+x)

convdir(".")
print "-----------------------------"
print "%d files are successfully converted, %d files are failed to convert." % (count_success, count_failed)

# vim: set ts=4 sw=4 sts=4 et: #

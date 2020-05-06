from time import gmtime, strftime
from datetime import datetime, timedelta,date
import os
import sys
import string

##### Defining log, sql file location using py script location #####
dir_name=os.path.dirname(os.path.abspath(__file__))
file_name=os.path.basename(sys.argv[0])
table_name=file_name.split('.')[0]
log_file=dir_name+'/'+table_name+'_log.txt'

##### Loading current datetime #####
curr_dt=strftime("%d-%m-%Y %H:%M:%S", gmtime())

###### Loading and writing on the log file ######
log_f=open(log_file, 'a')
log_f.write("\n")
log_f.write("######################################################")
log_f.write("\n")
log_f.write(curr_dt+":"+ table_name +" loaded")
log_f.write("\n")

### Running the required script #######
try:
    pass	
except Exception as e:
    er_msg=e
    log_f.write(curr_dt+": Script failed due to exception: "+str(er_msg))
    log_f.write("\n")
    log_f.close()
    msg='echo "'+table_name+ 'load failed with exception - '+str(er_msg)+'"'+'|mail -s"'+table_name+ ' - Failed" your_mail@server.com'
    sys.exit(1)

#!/usr/bin/env python3
import sys
import os
import string
from time import gmtime, strftime, sleep
from datetime import datetime, timedelta
import tarfile
import subprocess

def load_cron(cron_file):
    if os.path.exists(cron_file):
        subprocess.Popen('rm '+cron_file,shell=True)
        print(cron_file+' deleted')
    subprocess.Popen('crontab -l > '+cron_file,shell=True)
    sleep(2)
    print("Created cron file : "+cron_file)
    print('-------------------------------')

def job_list(cron_file):
    cron = open(cron_file,'r')
    cron = " ".join(cron.readlines())
    cron = cron.split('\n')
    jobs = []
    for _ in cron:
        if _.strip() == '':
            continue
        elif _.strip()[0] == '#':
            continue
        print(_.strip().split()[-1])
        jobs.append(_.strip().split()[-1])
    #print(jobs)
    return jobs

def create_tar(tar_file,jobs):
    if os.path.exists(tar_file):
        subprocess.Popen('rm '+tar_file,shell=True)
        print(tar_file+' deleted')
        sleep(2)
    print(tar_file)
    with tarfile.open(tar_file,"w:gz") as tar:
        for job in jobs:
            #print(job)
            try:
                print(job)
                tar.add(job)
                if os.path.exists(job.split('.')[0]+'_sql.txt'):
                    tar.add(job.split('.')[0]+'_sql.txt')
            except Exception as e:
                print(e)
                print(job)
        tar.add(cron_file)
        #tar.close()
    return True


if __name__ == '__main__':
    # Loading File Paths
    dir_name=os.path.dirname(os.path.abspath(__file__))
    file_name=os.path.basename(sys.argv[0])
    table_name=file_name.split('.')[0]
    log_file=dir_name+'/'+table_name+'_log.txt'
    cron_file=dir_name+'/'+table_name+'.txt'
    tar_file = dir_name+'/'+table_name+'.tar.gz'
    curr_dt=strftime("%d-%m-%Y %H:%M:%S", gmtime())

    # Logging Script Load Date
    log_f=open(log_file, 'a')
    log_f.write("\n")
    log_f.write("######################################################")
    log_f.write("\n")
    log_f.write(curr_dt+":"+ table_name +" load Started ")
    log_f.write("\n")

    load_cron(cron_file)
    jobs = job_list(cron_file)
    bkup = create_tar(tar_file,jobs)
    
    if bkup:
        msg='echo |mail -s"Live Cron Jobs Backup : '+ curr_dt.split()[0] +'" -A"'+tar_file+'" your_mail@domain.com'
        print(msg)
        subprocess.Popen(msg,shell=True)
        print('done')
    else:
        msg='echo "'+table_name+ 'load failed for - '+str("cron job backup")+'"'+'|mail -s"'+table_name+ ' - failed" your_mail@domain.com'
        os.system(msg)
        sys.exit(1)







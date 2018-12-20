backupdir=/SGRNJ/Database/backup/lab_sql
originfile=/SGRNJ/Database/test/1.11/lab_project/db.sqlite3
time=`date +%Y_%m_%d_%H_%M_%S`
backup_file=${backupdir}/${time}.sqlite3

#back up
sqlite3 ${originfile} ".backup ${backup_file}" 

#remove files 14 days 
#find ${backupdir} -name "*.sqlite3" -type f -mtime +14 -exec rm -rf {} \; > /dev/null 2>&1

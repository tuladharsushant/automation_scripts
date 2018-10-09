# automation_scripts

Here automation scripts readme.md consists of all the important details of automation. 

Automation_code_done_by: Sushant Tuladhar, Software Engineer, NCIT 
Program of code purpose: SynergyTech Software Automatic Mail Sender 
Significance: The significance of this code is to to send email without consuming too much effort in preparing sheets by connecting 
datbase with ssh connection and retrieving files in an order and manually managing them before sending. 

# The prequisites for using this automation scripts are written below as : 

1. Installation of python is very much essential for windows client with python version 3.4 or higher as syntax of programming
usually runs python3. 
2. Installation of pip (Python Install Packages) should be done for python3. 
3. In windows during installation environment variables should be checked and maintained to provide python and pip directory. 
4. Run the following through bash in linux. Bat file is under construction and will be available soon in directory. 
5. Python install packages requirement
 a) Pip install xlwt or pip3 install xlwt according to requirement # xlwt is for writing in excel xls file 
 b) pip install sshtunnel  #for SSHTunneling through SSHTunnelForwarder
 c) pip install PyMySql # for connecting database which could be local or used local transmission
 d) pip install smtplib #for sending email 
6. The another one of the important requirement is to turn on less secure apps on in gmail account to send it from bash. 
7. Run through bash by using following code where the script of .sh file is located :
  bash myfile.sh
8. The following steps occur when we use this automation script : 
 a) Enter database name 
 b) Confirm enter in the program or not 
 c) Then it asks for database password of remote database using SSH
 d) After this all the files are created in the local directory 
 e) Then the program asks for email address personal 
 f) Enter the password to continue
 g) Additional option that can be done in further update is choose the name of client where database is send. 
 
 
 #Example of the file when run : 
  a) Enter the name of database: mfin_dbname
  b) Are you sure you want to select this database 'mfin_dbname' type 'yes' or 'y' to continue and other characters for exit: yes
  c) Enter the password of level2 user: ************* 
  d) Filename generated occured according to timestamp value 
  e) Enter the email address of your gmail : mailadddress@gmail.com
  f) Enter the password of gmail here: ***************
  g) Enter the mail_sending address: mailbccc@gmail.com
  h) Prompts message :
    i) Successful sending message: 
      Mail sending successful with charge profile created
    ii) Unsuccessful sending message: 
      Mail sending failed. 
  
 
  

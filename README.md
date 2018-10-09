# Automation_scripts

Here automation scripts <code> readme.md </code>consists of all the important details of automation. 

<b>Automation_code_done_by: </b><code> Sushant Tuladhar, Software Engineer, NCIT </code><br> <br>
<b>Program code purpose:</b><code> SynergyTech Software Automatic Mail Sender </code><br> <br>
<b>Significance:</b> The significance of this code is to to send email without consuming too much effort in preparing sheets by connecting datbase with ssh connection and retrieving files in an order and manually managing them before sending. <br> <br>

# The prequisites for using this automation scripts are written below as : 

1. Installation of python is very much essential for windows client with python version <code>3.4 </code>or higher as syntax of programming usually runs python3. 
2. Installation of <code> pip </code>(Python Install Packages) should be done for python3. 
3. In windows during installation environment variables should be checked and maintained to provide python and pip directory. 
4. Run the following through bash in linux. Bat file is under construction and will be available soon in directory. 
5. Python install packages requirement <br>
a) Pip install <code>xlwt</code> or pip3 install xlwt according to requirement 
--# xlwt is for writing in excel xls file <br>
b) pip install <code>sshtunnel</code>  
--#for SSHTunneling through SSHTunnelForwarder <br>
c) pip install <code>PyMySql</code> 
--# for connecting database which could be local or used local transmission <br>
d) pip install <code>smtplib </code>
--#for sending email <br>

6. The another one of the important requirement is to <code>turn on less secure apps</code> on in gmail account to send it from bash. <br>
7. Run through bash by using following code where the script of .sh file is located :<br>
  <kbd> bash myfile.sh </kbd> <br>
  
8. The following steps occur when we use this automation script : <br>
a) Enter database name <br>
b) Confirm enter in the program or not <br>
c) Then it asks for database password of remote database using SSH <br>
d) After this all the files are created in the local directory <br>
e) Then the program asks for email address personal <br>
f) Enter the password to continue <br>
g) Additional option that can be done in further update is choose the name of client where database is send. <br>
 
 # Example of the file when run :<br>
 
 <b>a) Enter the name of database:</b> <code>mfin_dbname</code> <br><br>
 <b>b) Are you sure you want to select this database 'mfin_dbname' type 'yes' or 'y' to continue and other characters for exit:</b> <code>yes </code><br><br>
 <b>c) Enter the password of level2 user:</b> <kbd><code>*************</code></kbd> <br><br>
 d) Filename generated occured according to timestamp value <br><br>
 <b>e) Enter the email address of your gmail :</b><code> mailadddress@gmail.com</code><br><br>
 <b>f) Enter the password of gmail here:</b> <kbd> <code>***************</code> </kbd><br><br>
  <b>g) Enter the mail_sending address: </b><code>mailbccc@gmail.com </code><br><br>
  <b>h) Prompts message : </b><br><br>
  &nbsp;  i)Successful sending message: <br><br>
   &nbsp;&nbsp;  <code> Mail sending successful with charge profile created </code><br><br>
   &nbsp; ii) Unsuccessful sending message: <br><br>
   &nbsp;&nbsp;  <code> Mail sending failed. </code> <br><br>
 # end of file

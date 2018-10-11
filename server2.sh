echo "Welcome to server2 automatic mail generator " 
read -p "Give the name of database you want to connect: " dbname
echo "The database name is" $dbname 
read -p "Are you sure you want to continue with '$dbname'? Type 'yes'or'y' to continue or type other to exit: " value
if [ "$value" == "yes" ]
then
	 python3 /home/sushant/Desktop/exp.py $dbname
else
	echo "Program execution cancelled"
fi

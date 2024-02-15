## Add User Script ##
There is a Python script that automates the adding of Multiple users and groups to a Linux System.  This script will read from another file that contains a list of users that must be added to each system. Rather than manually creating each of these users this process has been automated by the .py file.
the 'create-users.py' script can be run in either of the following ways:
sudo ./create-users.py < create-users.input
 or
cat create-users.input | sudo ./create-users.py


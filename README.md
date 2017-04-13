## Project Purpose

Use Swiss pairing to create a match tournament
<br />
<br />
<br />


## How to use:
<br />
1. <a href="https://www.virtualbox.org/wiki/Downloads">Install VirtualBox</a><br />
2. <a href="https://www.vagrantup.com/downloads.html">Install Vagrant</a><br />
3. Get the FSND-Virtual-Machine.zip file from the repository<br />
4. Replace the files in tournament folder with the files on Github<br />
5. Redirect to vagrant folder: <pre>cd /vagrant</pre><br />
6. Run the following command to download the Linux operating system and install it: <pre>vagrant up</pre><br />
7. Run the following command to Login to the Linux VM: <pre>vagrant ssh</pre><br />
8. Run the following command to access the PostgreSQL database server: <pre>psql</pre><br />
9. Create a database in the server: <pre>CREATE DATABASE tournament</pre><br />
10. Run the following command to configure the database with new tables: <pre>\i tournament.sql</pre><br />
11. Finally, test the tournament.py utility <pre>python tournament_test.py</pre><br />



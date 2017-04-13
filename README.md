## Project Purpose

Use Swiss pairing to create a match tournament
<br />
<br />
<br />


## How to use:
<br />
1. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)<br />
2. [Install Vagrant](https://www.vagrantup.com/downloads.html)<br />
3. Get the FSND-Virtual-Machine.zip file from the repository<br />
4. Replace the files in tournament folder with the files on Github<br />
5. Redirect to vagrant folder: <pre>cd \vagrant</pre><br />
6. Run command: `vagrant up` to Login to the Linux VM<br />
7. Run command: psql and create database: `CREATE DATABASE tournament`<br />
8. Run command in psql: `\i tournament.sql` to create table in the database<br />
9. Finally, run `python tournament_test.py` to test the tournament.py utility<br />



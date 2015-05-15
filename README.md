##**Tournament Results**

##**Purpose of Project**

To have a Python module that uses the PostgreSQL database to track players and matches from a Swiss style tournament. This involves, "...defining the database schema (SQL table definitions), and writing code that will use it to track a Swiss tournament."

##**How to Obtain Code**

Assuming you are at my TournamentResults repo on Github, https://github.com/WebDesigner32/TournamentResults, click the Download ZIP button on the aside panel to obtain my code.

##**Technology Requirements**

1. PostgreSQL
2. Python
3. pyscopg2
4. bleach

##**How to Run Code**

1. Start Terminal and have vagrant folder in path at end.

2. Enter `vagrant up` and then enter `vagrant ssh`.

3. Enter `cd /vagrant/tournament`.

4. Enter `psql` and then enter `\i tournament.sql`.

5. Enter `\q` to quit.

6. Finally, enter `python tournament_test.py` to run the unit tests!

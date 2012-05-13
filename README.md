fibonboncheck
=============

Repository with fibonacci django application, modules and test scripts
It consists of the following files:

fiboncheck/ (main folder)
  webskripta.py (python script for fetching results from the django fibonacci app)
  senko/ (module folder for the fibonacci script)
    skripta.py (fibonacci script)
  fibonbon/ (django project)
    senko/ (folder containing the exact same skripta.py for django views to use)
    fiboncalc (the django application for returning html results of fibonacci)
    
To run the program, you need to have django installed. You can sync the django database with "./manage.py syncdb"
(it is set to use sqlite) if it doesn't work without the database (it should) and run the server 
e.g. ./manage.py runserver 8000 (or use apache or whatever).
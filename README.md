# global_dashboard_os project
Global Dashboard OS.

Steps:




General tools:
-------------
* Install Python (refer online doc)
* Install npm (refer online doc)
* If using VS Code install extensions (might like to install the ones with the highest download):
  * Prettier: code formatter
  * Python: Linting, Debugging (multi-threaded, remote)
  * Django: Syntax and scoped snippets

  * React: ES7 React/Redux/GraphQL/React-Native snippets (extension for React, Redux, and GraphQL in JS/TS with ES7 syntax)
  * JavaScript (ES6): Code snippets for JavaScript in ES6 syntax
* Install pip or pip3 or something equivalent as appropriate, if not already installed

* Command to install django and django rest framework:

    `pip3 install django djangorestframework`

Creating project and app:
-------------------------
* Command to create django project:

    `django-admin startproject global_dashboard_os`
Note: it creates folder with global_dashboard_os, which is a project folder. Inside this project folder, there is a folder with the same name and that contains configurations.

* In order to create application within project, from inside project folder run command:

    `django-admin startapp global_dashboard_os_api`
Note: observe the contents inside app folder; these are different from project subfolder's contents


Running a project:
------------------

* After making changes, run below commands:
  * `python3 ./manage.py makemigrations`; whenever we make changes to DB or models we need to run this. Might need to run this when running the project for the first time just to initialize the DB. Django stores admin related data in a built-in DB. 
  *  `python3 ./manage.py migrate`; if running app for the first time, this will initialize admin data. Note: After running this command, we should be able to see `db.sqlite3` or its equivalent in the project folder.
  

Running server:
---------------
* Run the command:
  * `python3 ./manage.py runserver`. Note: If the setup is correct, we should be able to see something like:
  ```text
    Django version 5.2, using settings 'global_dashboard_os.settings'
    Starting development server at http://127.0.0.1:8000/ 
    Quit the server with CONTROL-C.
  ```
* If we click on the url, it should take us to browser and render the content returned by HttpResponse in the current setup.


Server auto-refresh:
--------------------
* Django automatically reflects the changes made in source code. To test this, if we make some changes to the main function and save it, we should see server re-running.  


Installing and using Django debug tool bar:
------------------------------------------
* https://django-debug-toolbar.readthedocs.io/en/latest/


Frontend/UI app setup:
----------------------

* Check if npm is installed, if not install it. Also install node.js if not already installed. Instructions can be found online. 
* Create new app within the project
  * `django-admin startapp global_dashboard_os_frontend`

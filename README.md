# itemscatalog1
To create restaurent Menu application where any user can make changes like add delete the restaurents and the food items of each restaurent.

#What we Need

1 Python 2.7
2 Vagrant
3 VirtualBox
4 Oauth

### How to Run
Install virtualBox and vagrant and clone the repositorey unzip the itemcatalog1 folder in vagrant diractory login to vagrent initialise database and launch the application after that go to your favourite browser and type in localhost:5000 and run it and enjoy the application.

#How to use google login?
1) Go to google dev console, If you have a login credentials or signup and then do it.
2) Select Create Crendentials > OAuth Client ID
3) Select web application.
4) Authorized JavaScript origins = 'http://localhost:5000' 
   Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
5) Create.
6) You can have client Id copy the id and paste it on login.html file.
7) Download Json file and keep it in the folder containing .py files.
8) Run the project.py.

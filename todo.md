TODO: 
===
## immediate future
- set this instance's admin password to an enviroment variable
- add Ultimatum Game: 2 players, 5 rounds, 100 points = 10 cents
- ~~test exitcodes in otree 2.X~~
    - ~~make exitcode app crosscompatible~~
- diagnose bug when otree-connect ing: 
- 
        Exception calling "GetCookies" with "1" argument(s): "This operation is not supported for a relative URI."
        At C:\Home\PowerShell\Supervisor\PSOtree\Otree.ps1:107 char:5
        $cookies = $OtreeSession.Cookies.GetCookies($loginUrl)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
        FullyQualifiedErrorId : InvalidOperationException
- test otree 2 on heroku!
- write up how to create heroku setup using the cli from a readymade git repo
    - note: dependencies need to be in the right place
    - [official otree-heroku docs](http://otree.readthedocs.io/en/latest/server/heroku.html "Basic Server Setup (Heroku)")





















 <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br /> <br />
https://docs.djangoproject.com <br />

6)	oTree in the Lab<br />
a.	Integrate oTree based on oTree Launcher with DeSciL LabLauncher. Otree server needs to run standalone on descil-sup01. Deliverable is a PowerShell script that prototypes startup of an oTree server on a Windows box with sqlite Database. [MILESTONE 10]<br />
b.	Integrate oTree on descilix to run as the lab server. Milestone is reached with a polished PsLabLauchner script that starts an otree experiment in the lab. [MILESTONE 11]<br />
c.	Implement project 0000-OTreeDemo, a DeSciL standard treatment hosted on DeSciL infrastructure based on Guess-60 or ‘Rock-Paper-Scissors’ that implements and demos browser bots. The milestone is reached if I can see a properly working test suit running through on all 45 DeSciL Client computers. [MILESTONE 12]<br />
d.	oTree on a stick. You will receive 1 USB Stick. Install oTree in a virtual environment that can be run from the USB Stick. The milestone is reached if you provide a PowerShell script that creates the stick [MILESTONE 13]<br />
7)	oTree Core Hacks<br />
a.	Implement Access-Code Exit-Code procedure. Extend oTree data model to generate an exit code at the same time the access links are generated. This list of codes needs to be downloadable as JSON from a running oTree instance. [MILESTONE 14]<br />
b.	Provide an overview of oTrees capabilities for exit web-hooks. oTree can, for example, navigate to an URL after participants have completed. Prepare a routine that makes a WebApi call to DeSciL’s TurkR Webservice to check-out and offload bonus payments. Specs follow. [MILESTONE 15]<br />

STAGE 2 (aka “Get productive and profitable”)<br />
8)	oTree on the AMT<br />
a.	Prepare the ‘Rock-Paper-Scissors’ treatment for a group size of 2 for deployment on Amazon Mechanical Turk. Run this treatment with increasing session sizes together with DeSciL Lab Staff, i.e. Oliver. Budget 50$, i.e. 100 assignments for 0.5$. Provide a little statistical analysis if rock, paper, or scissors has highest chance of winning . [MILESTONE 16]<br />
9)	oTree REST API<br />
a.	I would like to be able to setup, start, stop, download codes and data from oTree remotely by means of REST calls, i.e., with PowerShell. Design a WebApi Backend endpoint based on Django. Let me your review your design document that is a write-up in Markdown in the otree-descil repo. [MILESTONE 17]<br />
b.	Build a first prototype and proof-of-concept. [MILESTONE 18]<br />
c.	Introduce yourself to Mariyana and Dinesh. They develop an application with Django backend and Angular frontend that is hosted on descilix. Explain them what you changed on Descilix. Try to find out who to standardize Django workloads on descilix in general. Git is your friend. [MILESTONE 19]<br />
11)	Implement Market Game for Martin [New Repo with its own Milestones]<br />
12)	Implement and run a Market Game for Jonas Gehrlein (University of Bern), [New Repo with its own Milestones]<br /><br />
13)	Integrate, test, and run a treatment developed by the Rauhut Group (University of Zurich), [New Repo with its own Milestones]<br />

STAGE 3 (aka “Let’s see how far we come”)<br />
14)	Implement and run a treatment for the Diekmann/Wehrli aka TimedVOD.<br />
15)	Implement an oTree treatment ‘Rock-Paper-Scissors’ and provide it push upstream to otree repo.<br />
16)	Implement and test run an SVO Slider treatment. Port slider widgets from nodeGame to oTree. Push upstream.<br />
17)	Identify and prepare for “oTree-as-a-Service”. <br />
18)	Deploy oTree to IIS and MSSQL, i.e., you have to swap the webserver and the database.<br />
19)	Dockerize oTree.<br />
20)	Deploy oTree to Azure and AWS. Azure Traffic Manager. Pimp descilitics.com .<br />
21)	Performance and service monitoring. Suggest proper tooling.<br />

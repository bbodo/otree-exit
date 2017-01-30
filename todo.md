TODO

1:
otree treatments a-z
econworld oder so

2:
otree rooms vs waitingrooms vs labels vs accesscodes vs exitcodes

3:
otree subdirectory problem,
bzw. database resets vs migrations

5:
bash for windows ubuntu shizzle

6:
investigate venv

https://docs.djangoproject.com <br />
3)	Program a first oTree Game<br />
a.	Take the example ‘Guess 2/3’ and make a Guess 60% game out of it, deploy it locally, let me and Martin play/see it on your laptop/machine. [MILESTONE 1 ]<br />
4)	Deploy oTree to www.descilix.ethz.ch<br />
a.	I will provide credentials to descilix. Get comfortable with bash.<br />
b.	Make a plan what needs to be installed. Let me review.<br />
c.	Install Python/Django prerequisites.<br />
d.	Use MySQL / MariaDb instead of PostgreSQL.<br />
e.	Let Martin and me play Guess-60 on gunicorn on port 8080. [MILESTONE 2]<br />
f.	Use nginx as a front end for otree. Make a plan what needs to be configured. Let me review. Let us Martin and me play Guess-60 on <br />
g.	Write a documentation what you have installed. Automate your install procedure with a build script. [MILESTONE 3]<br />
5)	GIT and Visual Studio Code. Prepare version control for the rest of us.<br />
a.	Start committing your materials, documents and build scripts to the otree-descil repo. I expect that from then on we can watch your progress there. No commit, no progress.<br />
b.	Add one/few markdown pages that summarizes the resources you have consulted to come this far. Add this to the repo.
c.	Add the Guess-60 to the repo. [MILESTONE 4]<br />
d.	Update the cloned oTree repo in the DeSciL Org from upstream. Additionally, clone the otree-core and otree-launcher repos. Document how you did this and add your findings as markdown page to otree-descil repo. [MILESTONE 5]<br />
e.	Install Visual Studio Code, clone the repo from GitHub. Make a change and commit from Visual Studio Code [MILESTONE 6]. <br />
f.	Install vscode python extension. Play around with the code and with code completion. Write a short blog post (1 page) ‘How-to use Visual Studio Code to program oTree treatments.’ [MILESTONE 7].<br />
g.	Re-Setup this tasklist as GitHub Issues and a GitHub Project. We want this project managed with their. Kanban boards. [MILESTONE 8].<br />
h.	Explain und help Martin and me how we do a pull-request. Let us change a page in the documentation. Milestone is reached if it is easy for both of us to do PRs. [MILESTONE 9].<br />
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
d.	Introduce yourself to Chris Wickens, lead programmer of oTree. Demo your prototype and let him review and comment. You can also invite all other oTree programmers to this [MILESTONE 20 ]<br />
10)	Provide an ‘oTree’ entry to the DeSciL knowledgebase.<br />
a.	This should describe how people at GESS get startet with oTree. This reports your entire DeSciL efforts towards oTree and gives an overview of what is possible, what not, not yet, and what has been accomplished overall. You might want to start with this earlier. This is the end product you have to provide towards Prof. Hölscher. [MILESTONE 21].<br />
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

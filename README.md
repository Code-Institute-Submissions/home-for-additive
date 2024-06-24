![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


# HOME FOR 3D

## INTRODUCTION

Welcome to the 'Home for 3D' project. The projecs is the platform presenting informally and UNOFFICIALLY the 3d metal printing research group of the School of Mechanical Engineering, University of Portsmouth (UoP), UK. The purpose of the project is to facilitate interaction between the research staff of the Team and the students interested in learning more about the fascinating and explosively growing area of metal 3D printing (a.k.a. additive manufacturing). Are you interested? Here you can meet the key people, learn what they do. Do you have your own idea? Share it with us: sign-up and submit your proposal.

## TECHNOLOGIES

The following tools were used during the project setup and development
- Static frontend: HTML, CSS, JavaScript
- Backend: Python
- Relational database: PostreSQL
- Frameworks: Django
- Libraries: Bootstrap, Google Fonts


## USER STORIES PROJECT REQUIREMENTS

The project must (will) provide the followith main capabilities:

- The user will found the initial information on the group (members and their background).

- The user will be able to sign in and submit an idea in the form of written proposal.

- The user will receive a feedback on the submitted idea.

- The platform will provide a channel for informal communication (e.g. will be able to enquire regarding current status of an experiment, planned/unforeseen equipment maintenance and downtime, etc.)

## FEATURES
The ingormative part describes the research group focusing of 3D metal printing. Therefore, it was decide to select cold, gray-ish color theme resembling the color of metal powder used for the process. The layout is responsive, depending on the device you use to access the content.
### Template
#### 1. Navbar
![Navbar-large-screen]()<br>
Navigation bar on a regular pc screen.<br>
![Navbar-mobile-device]()<br>
Navigation bar on a mobile device.<br>
Navigation bar allows to navigate between:
- Home
- Team
- Facility
- For students<br>
tabs.
#### 2. Footer
![Footer-large]()<br>
Footer on tegular pc screen<br>
![Footer-mobile-device]()<br>
Footer bar on a mobile device.<br>
Footer contains brief description of the Group, useful links and 'further reading' link.
### Content
#### 1. Static content
Home, Team, Facility tabs: information about the group, expertise and available lab equipment.
#### 2. Dinamic content
Tab student will take you to the list of submitted proposals (also responsive).


## STRUCTURE
1. Home<br>
External links:<br>
 - Further reading
 - Youtube
 - University (Home)
 - Wikipedia<br>
2. Team<br>
Same external links as above via template.
3. Facility<br>
Same external links as above via template.
4. For Students<br>


## DATA MODEL


## ACCESS LEVEL RESTRICTION
- Access to an informative part of the site and see the titles and student names: any visitor.
- Access to full text of all proposals: any registered and logged in student.
- Submit, edit and delete proposals: a particular student under his own credentials.

## VALIDATION
HTML, CSS, Python and JS files were validated using W3C, Jigsaw, PEP8 CI Linter and jshint (respectively). Validation tests passed with no errors or warnings. The testable html code was accessed from renderred pages using the Ctrl-U key. The code then was copied into the direct input textfield of W3C validator.

## LIGHTHOUSE

## TESTING

## DEPLOYMENT

## FUTURE WORK

### Acknowledgement
The code was written and debugged using the desktop version of VS Code

==================================================================





Welcome DrSYakovlev ,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **April 26, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


# HOME FOR 3D
![responsivity overview](./static/images/responsivity.jpg)<br>

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
![Navbar-large-screen](./static/images/nav-bar-large.jpg)<br>
Navigation bar on a regular pc screen.<br><br>
![Navbar-mobile-device](./static/images/nav-bar-mobile.jpg)<br>
Navigation bar on a mobile device.<br><br>
Navigation bar allows to navigate between:
- Home
- Team
- Facility
- For students<br>
tabs.
#### 2. Footer
![Footer-large](./static/images/footer-large.jpg)<br>
Footer on tegular pc screen<br><br>
![Footer-mobile-device](./static/images/footer-mobile.jpg)<br>
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
List of proposed ideas<br>
Options: log in or sign in:<br>
![Logged-out user](./static/images/log-in-invite.jpg)<br><br>
If logged in or signed in:<br>
a. Can see any proposal
b. Can submit, edit and delete your own proposal<br>
![data-form](./static/images/proposal-form.jpg)<br>
Form for proposal submission/edit<br><br>
c. Log in status is shown<br>
![log-in_status](./static/images/log-in-status.jpg)<br>
![log-in_status](./static/images/log-in-status-1.jpg)<br><br>
If 'Delete proposal' option is selected, the user has a chance to confirm:<br>
![delete-confirm](./static/images/delete-confirmation.jpg)<br><br>
If the user creates or changes a proposal, notification message is shown and the user can navigate back to the list page:<br>
![data-change-confirm](./static/images/create_edit_confirm.jpg)<br>

## DATA MODEL
The database table (model) describing the structure of submitted proposals are shown below.<br>
![data-model structure](./static/images/db-table.jpg)


## ACCESS LEVEL RESTRICTION
- Access to an informative part of the site and see the titles and student names: any visitor.
- Access to full text of all proposals: any registered and logged in student.
- Submit, edit and delete proposals: a particular student under his own credentials.

## VALIDATION
HTML, CSS, Python and JS files were validated using W3C, Jigsaw, PEP8 CI Linter and jshint (respectively). Validation tests passed with no errors or warnings. The testable html code was accessed from renderred pages using the Ctrl-U key. The code then was copied into the direct input textfield of W3C validator.

## LIGHTHOUSE

## MANUAL TESTING
![test](./static/images/testing.jpg)


## DEPLOYMENT
The project was deployed on [heroku.com](www.heroku.com). After creating the user account the following steps were undertaken to deploy the project.
1. 

## FUTURE WORK

### Acknowledgement
The code was written and debugged using the desktop version of VS Code. The aurthor thanks the School of Mechanical Engineering, University of Portsmouth for providing textual and picrorial content and the Code Institute for providing the template.


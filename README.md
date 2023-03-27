# djangoProject
A django project created using pycharm, database, HTML and CSS. 
The project contains pages where it is possible to create new users, log in to existing users, create questions and choices.
Log in to existing accounts, sign up for new accounts.
A page for reset passwords.
Polls page where displays the options for voting.
Admin page with access to edit the questions, choices and users.
# Features
Manual testing and automatic testing procedures were added to this project using positive and negative testing, the test includes functions to ensure that everything is working properly.
To enhance the security of the web application, multiple additional measures were implemented. The application was fortified against SQL injection attacks. Additionally, it used multiple HTTP security headers to protect against XSS (Cross-Site Scripting) attacks, as well as the redirection security header to automatically redirect users to the HTTPS version of the site, which facilitates the prevention of eavesdropping and man-in-the-middle attacks.
To prevent CSRF (Cross-Site Request Forgery) attacks, which occur when an attacker takes advantage of a website user's trust to perform unwanted actions on the user's behalf. Django's built-in CSRF middleware was used. At last, the transaction.atomic() was used to ensure that all database operations associated with a single transaction were executed as a unit. This not only ensures reliability but also minimizes the chances of data theft in the occurrence of errors. The safety of the service was increased to minimise the chances of hacking attacks by incorporating these security protocols.

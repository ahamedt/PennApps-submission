# PennApps-submission

Instructions:
I laid out the directory structure exactly the way I was using it as I was developing the site. So download first and the root directory should be names "BlogApp" not "PennApps-submission". 

From the command line, go to the directory containing "manage.py". From this directory, run python manage.py runserver (for some reason, the command didn't run on my machine unless I ran sudo python manage.py runserver. Try that if it gives an error, like if it says that port is being used elsewhere). ** If its a port error, run sudo python manage.py runserver 8001. It can be another number or another port that isn't occupied (doesn't have to be 8001).

Once the server is running, you will be at the sign in page, and then you will have the option of making an account. Make an account and you can then access the home page.

NOTE: For password reset functionality, you need to go to settings.py and choose a host email. Enter the host email in EMAIL_HOST_USER and the email's password in EMAIL_HOST_PASSWORD. Then, at least for gmail, you go to gmail apps password and then you need to allow sign ins from less secure apps. That will then enable the password reset functionality. Otherwise, an error screen should pop up when you try to submit the form to reset. You reset from the login screen.

Known Bugs:

Although I don't think there are major bugs in the functionality, one thing that was left because I ran out of time was that posts, if the user doesn't choose a image, simply post the default profile picture image.

There also isn't a check on "real" emails. (Someone could make an account with an email like bruh@bruhmoment.com). This primarily affects the password reset function, which would in turn be sending an email to a nonexistent email account.


Implemented Features + Additional Challenges:

Users on this app are able to create an account for themselves and post on the platform, where their post, their username, and the date posted are depicted. Basically all of the features of the base program given in the challenge document, alongside:

* Styles with HTML and CSS -> All pages utilize HTML and CSS (bootstrap4) styling. base.html serves as the base html document from which the majority of the html pages inherit from. The navbar was also made/styled with bootstrap4.

* Allow user to like and tally up likes -> Users are able to like posts that other users make and see how many likes a given post has. This is done by accessing the DetailView of the post by clicking on the Post's caption. A blue like button will be above the post, with the number of likes to its right.

* Allow users to post pictures alongside their posts -> Each user posts a picture alongside a caption for their picture. 

* User Profile -> When each user is registered, a profile is generated that they can access when logged in. This profile includes their profile picture, their username, and their email. It also includes an additional form if they wish to change any of those parameters

* Reset Password -> Users are able to reset their Passwords. This is done from the login page. Once settings.py is properly configured (SEE ABOVE), then submitting the password reset form should send an email to whatever email you signed up with your account. This might appear in spam from the localhost. Following the link should lead you to a form to reset your password.

* Delete Posts -> Users have the option to delete their own posts by going to the detail view of the post and clicking the red delete button. This will remove the post and the associated picture.

General Thoughts + Feedback:

Personally I thought that this was a very rigorous challenge for me as before the only experience with web development I had was primarily in basic Flask. I did not know any django going in, so I relied alot on various Youtube tutorials, stackoverflow posts, and random websites on the internet to figure out my errors. The forms an d html was particularly daunting, so I relied on my tutorials and stackoverflow posts in order to get a sense of how I am able to style them, and thus I was able to create my html files as a combination of all of the posts that I saw that detailed how to make forms and webpages and style them with css. I did learn more than what I had originally anticipated, such as in the case of view functions, CBVs, Requests, and how webpages function dynamically. Overall I thought that it was a good challenge, but it did take me more time than the expected amount originally recommended.



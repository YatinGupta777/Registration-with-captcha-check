# Registration with captcha check
 
Hi, I have named the app "reg" which handles the process.

I have considered two models in models.py :
1. One for user which store user's name,email and password.
2. IpCount: Which manitains the ipvisited with their count on the last day or if the count exceeded 3 on any day.

Views.py handles all the functionality.
Forms.py takes the model to make it a form.
Urls.py handle url activity.

Every registration attempt (clicking on signup) is noted using ajaxrequest to django which increments the countof IP without reloading the page.
If captcha check fails page is reloaded to show the invalid captcha message and prevent to save the form.

Validations assumed on form field :
1. All the fields are required.
2. Email has to be unique.
3. Password can be anything
4. Captcha shown as required.



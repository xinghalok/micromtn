Get Your Flask Apps Up And Running Fast on EC2
Web development

Get Your Flask Apps Up And Running Fast on EC2
---------------------------------------
Lately there have been a spate of articles detailing how to deploy Flask applications on Amazon Web Server's EC2 instances. However, when I followed these guides to deploy this very website, I often ran into errors, omissions, and edge cases that were not covered by the article. Hours of yak-shaving ensued. The application I wanted to host was not a massive project - it was a simple blog! It didn't really make much sense to me that hosting it should be such an endeavor, especially considering how swift Python development usually is for me.

Essentially this article exists as a quick antidote to such pains. I am going to show how you, dear reader and aspiring Python webdev, can get your Flask app running on the net. 

Prerequisites
--------------
+ You have an <a href="http://aws.amazon.com/">AWS account</a> with an EC2 instance running Ubuntu
+ Python and Flask are installed on this system
+ Your Flask source is stored in a git repo 
+ You have not gone blind by the time you reach the end of this sentence.

Geronimo!
---------
Log in to your EC2 instance (Usually done through an SSH connection) and type the following command:

    sudo apt-get install apache2 libapache2-mod-wsgi

This installs our webserver, Apache2, as well as a Python WSGI module. Don't worry if you do not know what a "WSGI module" is right now; you can learn about it <a href="http://code.google.com/p/modwsgi/">here</a>. Essentially what it does is hand over  Python's built-in webserver duties to Apache.

If your point yourself to your EC2 domain (either the DNS address you used to connect to your server via SSH or a URL you have pointed towards it), you will see a welcoming message from our good, if homely friend, the Apache webserver. Lets get your Python app on there. 

Type the following:

    sudo mkdir /var/www
    cd /var/www
    sudo git clone url://to.your.git.repo
    cd yourgitrepo
    sudo nano yourflaskapp.wsgi

The .wsgi file should match the name of the Python file containing the <raw>"yourflaskapp = Flask(\_\_name\_\_)" </raw>line. Make sure that in this file (the main python file, not your newly-created .wsgi file), you have any yourflaskapp.run() calls contained within the <raw> "if \_\_name\_\_ == '\_\_main\_\_':"</raw> clause. Otherwise, your app will be starting a local WSGI server instead of forwarding it through mod_wsgi and Apache.

The yourflaskapp.wsgi file is simple and should look like the following:

    import sys
    sys.path.insert(0, '/var/www/yourgitrepo')

    from yourflaskapp import yourflaskapp as application

Note that 'application' is NOT a placeholder name. If you do not import it as that, mod_wsgi will spit up on you. 

Now, type the following commands:

    cd /etc/apache2/sites-available/
    sudo nano sitename.com

where sitename.com is whatever you want your site to be called. The contents of this file should look like this:

    <VirtualHost *:80>
    	     WSGIDaemonProcess yourflaskapp
	     WSGIScriptAlias / /var/www/yourflaskapp/yourflaskapp.wsgi

	     <Directory /var/www/yourflaskapp>
	     		WSGIProcessGroup yourflaskapp
			WSGIApplicationGroup %{GLOBAL}
			Order deny,allow
			Allow from all
	     </Directory>
    </VirtualHost>

Then all that is left do is disable the Apache default page and enable your Flask app:

    sudo a2dissite default
    sudo a2ensite sitename.com
    sudo service apache restart

Now if you navigate to your page, you should see your Flask app up and running. Congrats. That took about 10 minutes, I hope. Of course, this just barely scratches the surface of the power and flexibility of apache2 and mod_wsgi, but those are topics you and I will <a href="http://sleepy-headland-2831.herokuapp.com/">exploring more</a> as we go on to build bigger web apps.

The beauty of this approach is not only that it is fast and relatively painless (I could write a shell script that would make this a 10 second process...hmmm), but it is also quite modular. Simply rinse and repeat these steps for individual apps and you can switch between them using a2dissite and a2ensite. If you have more than one URL redirecting to the EC2 instance, you can configure Apache2 to serve each one by way of creating unique sitename.com configs as done above.

If you have any questions, be sure to email me at me.anzuoni at gmail dot com.



 




  

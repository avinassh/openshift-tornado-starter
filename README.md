# Hello!
This is a very simple package which should get you started on Openshift with Python Tornado. Knowledge of Python or Tornado is not required to deploy.

It can be used for serving a static blog or your personal portfolio page etc. You can check the [demo](http://tornado-avinash.rhcloud.com/) here

# Instructions:
 - If you are using openshift web interface, pick [Python 2.7 cartridge](https://openshift.redhat.com/app/console/application_type/cart!python-2.7) and provide url of this repo in `Source Code` field. Thats all!  
 - If you are using `rhc` then run following:

		    rhc create-app appname python-2.7 --from-code https://github.com/avinassh/openshift-tornado-starter.git

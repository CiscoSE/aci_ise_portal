**ACI and ISE Portal**

This tool automates the configuration necessary to support user authentication using 802.1x and RADIUS with ACI and ISE.


HTML user interface works better in Chrome and Firefox

Contacts:

* Cesar Obediente ( cobedien@cisco.com )
* Santiago Flores ( sfloresk@cisco.com )
* Jason Mah ( jamah@cisco.com )

**Container Installation**

docker run -p 8080:8080 jasmah/aciiseportal

go to http://0.0.0.0:8080


**Source Installation**

As this is a Django application you will need to either integrate the application in your production environment or you can get it operational in a virtual environment on your computer/server. In the distribution there is a requirements.txt file that you can use to get the package requirements that are needed. The requirements file is located in the root directory of the distribution.

It might make sense for you to create a Python Virtual Environment before installing the requirements file. For information on utilizing a virtual environment please read http://docs.python-guide.org/en/latest/dev/virtualenvs/. Once you have a virtual environment active then install the packages in the requirements file.

(virtualenv) % pip install -r requirements.txt

To run the the application execute in the root directory of the distribution:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:YOUR_PORT


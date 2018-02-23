==============
flask_platform
==============


Creates a simple flask app that integrates the systeminfo package (https://github.com/RobertDebhal/systeminfo)
to display system info for you computer in a web browser.

Description
===========

Note: Flask is required for this package to run and is automatically installed with this project if you do not 
already have it installed.

Usage: After installing the systeminfo project and the flask_platform project you may type systeminfo into the 
command line which shall run the flask app on port 5000 and listens for traffic on all IPs.

You then type your-IP-address:5000 or localhost:5000 (if using a local browser) into the browser and information
about your computer shall be displayed.

Note
====

This project has been set up using PyScaffold 3.0.1. For details and usage
information on PyScaffold see http://pyscaffold.org/.

Install python 3, pip

To install dependencies create a new venv in the project root folder
-- cd <projectfolder>
-- python3 -m venv venv
--pip install -r requirements.txt
This will install all dependencies for the project



Note: Tests are restricted to the flows giving a 200 response code. It is assumed that feeding improper data will provide a 4** response

Libraries/Framework
------------------
Pytest
JSON
Requests

Files
---------------
test_input.py --> Tests
conftest.py --> utilites
time.json--> time values in epoch format (max values upto 10) 
baseurl.json--> the URL from which all other subsequent resource URL are derived
check.py--> A file where unit tests can be implemented in case execution fails, to ensure whether all utilities are working fine or not


How to Execute
----------------------
cd <project folder>/test
--pytest (gives result)
--pytest -v (gives verbose result)


Tests implemented:
Scenario 1
position of two satellites in two times and units as miles
    This test will run once and display all the results upto 10 values of times (as described in the documentation).
    Values asserted are status code, name, ID and timestamp.     
    User can input maximum ten time values and minimum of one value in the time.json file
    In a single execution, details in the response will be validated. This actually saves time in a scenario where there are ten times and user has to execute the test ten times

Scenario 2
position of two satellites in two times and units as kms
    The same test set up as above is implemented here also. unit is changed as kilometers.

If there are more units coming up other than miles and kilometers, that can also be parametrised.

Scenario 3
check tles data output in JSON format
Validates the ID, name and status code
    
Scenario 4
check tles data output in text format
    Validates the length of the text response is 3. As two times are given, in text format the results will be displayed in three lines
    Validates whether ISS, satellite is present in the text response
 

Test cases can be written more with testing individual times in one test case, but that is already achieved. 


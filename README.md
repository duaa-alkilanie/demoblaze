# demoblaze


Install Python 3 , V.3.8

Install PyCharm or any other preferred python editor

Running test-suite


Create virtual env. using below command

python -m venv venv


show all plugin:


python -m pip list



Running pytest :


python -m pytest



(Install test-suite dependencies using below command)


pip install -r requirements.txt


#Disbale warnings


pytest -s -v --disable-pytest-warnings -m GET   tests
or
add pytest-ini_file


#to generate report.xml

install  pipenv install pytest-xml
run % pipenv run python -m pytest -v --junitxml="JSONPlaceholder.xml"
#to generate report.html
pip install pytest-html

Run the command :
pytest --html=report.html.


test cases : 
1- test_login_with_invalid_password
2-test_login_with_valid_data
4- test_sign_up_with_valid_data
5-test_sign_up_with_data_already_exist

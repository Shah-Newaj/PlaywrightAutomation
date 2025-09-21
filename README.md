# PlaywrightAutomation
Practice Playwright with Python and Pytest

Command to run the framework file...

    pytest -v -s .\test_framework_web_api.py

Command to run in the specific browser...

    pytest -v -s .\test_framework_web_api.py --browser_name chrome

Command to run selected tests ...
     
    pytest -m smoke 

Command to run test in parallel ... 

    pytest -n auto

    pytest -n 4

Command to trace execution ... 

     pytest -n 4 --tracing on --html=report.html



Used Packages in this Project...

certifi	2025.8.3

charset-normalizer	3.4.3

colorama	0.4.6

execnet	2.1.1

greenlet	3.2.4

idna	3.10

iniconfig	2.1.0

numpy	2.3.3

packaging	25.0

pandas	2.3.2

pip	25.2

playwright	1.55.0

pluggy	1.6.0

pyee	13.0.0

pygments	2.19.2

pytest	8.4.1

pytest-base-url	2.1.0

pytest-playwright	0.7.0

pytest-xdist	3.8.0

python-dateutil	2.9.0.post0

python-slugify	8.0.4

pytz	2025.2

requests	2.32.5

six	1.17.0

text-unidecode	1.3

typing-extensions	4.15.0

tzdata	2025.2

urllib3	2.5.0

xdist	0.0.2

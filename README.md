#### PHPTRAVELS Automated Tests

**Compatibilty:**

Windows - Chrome v79

Mac - Chrome v78


**Build instructions:**
1. Have Python 3.x and PIP installed on your device
2. Clone the repo
3. Navigate to project root:

    `cd <PATH_TO_PROJECT>/PHPTRAVELS_Ttests/`
    
4. Install dependencies from requirements.txt :
    
    With PIP:
    
    `pip install -r requirements.txt`
 
5. Execute /run_me.py
 
     `python run_me.py`

The program was developed on windows



 
 **Understanding the project's files:**
 
 /execution - Should contain different methods of running tests. Currently holds 1 method.
 
 /reports - HTML test reports are saved here
 
  /resources/chromedriver - Here lies the chromedriver binaries. If you don't have chrome updated to the versions stated above,
  you can replace the files with relevant ones from https://chromedriver.chromium.org/downloads

 /resources/infra - Contains Page Object Models, and the Browser class
 
 /resources/settings - base_settings.py contains the project paths and url. run_settings.py should hold parameters regarding the test execution, only one relevant for  now.
 test_settings.json states whether the tests will run headless or not, and which test are to run.
 This format is designed allow receiving a settings JSON externally.
 
 /tests/base_tests - The test case superclasses. ParametrizedTestCase adds the option to send parameters into test cases (see "param" in code),
 and BaseTest adds the functionality relevant for a Selenium project.
 
 /tests/test_cases - Test logic files. All designed to work with provided test data and won't run on their own.
 
 /tests/test_data - JSONs that provide the test case data. The project is designed to read all data provided within these files, in case the corresponding test was provided in test_settings.json
 Planned this way to allow receiving these JSONs from an external source.
 
 /tests/test_data/test_utils.py - A collection of functions that mostly help extract and aggregate test cases.
 
 /src - This directory was added after importing the HTMLTestRunner from a private github repository. The main project was abandoned and this version provided more functionality.
 
 /run_me.py - A CLI / entry point for a build tool.
 
 **Given more time I would:**
 
1. Build the project into a standalone executable
2. Add more assertions regarding the page integrity. Incuding base page properties that will provide more info on the top and bottom panels.
3. Parametrize FlightTests more thoroughly (Modify every field)
4. Annotate the Page Object Modules, but I do think they are pretty self explanatory
5. Give test cases a unique name in favor of report analysis
 
 
 
 
 

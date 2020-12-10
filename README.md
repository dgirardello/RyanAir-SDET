# RyanAir-SDET

## Requirements
- Python3
- Pip3
- Venv
- Selenium ChromeDriver (https://chromedriver.chromium.org/downloads)

## Installation
1. Download the repository
2. Create a virtual environment
   ```commandline
   python3 -m venv ./venv
   ```
3. Activate the virtual environment
   ```commandline
   source venv/bin/activate
   ```
4. Install the required libraries
   ```commandline
   pip3 install -r requirements.txt
   ```
## Running tests

To run the tests simply execute 
```commandline
behave features/
```
This will execute the test scenarios and at the end of the test run summary will be shown    
```commandline
1 feature passed, 0 failed, 0 skipped
10 scenarios passed, 0 failed, 0 skipped
57 steps passed, 0 failed, 0 skipped, 0 undefined
Took 1m20.671s
```

## Output
Several output options are available using the **-f** option 
I.E.: If you don't wish to see all the test execution you can use the *progress* formatter
```commandline
behave features/ -f progress 
```
This will print a dot for every scenario executed (or an F if the scenario has failed) and print the execution summary, like this
```commandline
features/booking.feature  ........
1 feature passed, 0 failed, 0 skipped
10 scenarios passed, 0 failed, 0 skipped
57 steps passed, 0 failed, 0 skipped, 0 undefined
Took 1m19.434s


```
To which output format are available execute
```commandline
behave -f help 
```

### Behave configuration
Several parameters can be configured, for that edit the file Behave.ini

User email and password for login
```ini
ryanair_user=<USER EMAIL>
ryanair_pass=<USER PASSWORD>
```
Browser to be used, only Chrome or Firefox are available at this point 
```ini
browser=Chrome
```
_**Note:**_ The correct WebDriver mus be installed and in the path to be used
| Browser | Web Driver | URL |
|:-------:|:----------:|:---:|
| **Chrome** | ChromeDriver | https://chromedriver.chromium.org/downloads |
| **Firefox** | GeckoDriver | https://github.com/mozilla/geckodriver |

In some cases the internet connection may be too slow and timeouts may occur, to solve that set the parameter `slow_connection` to `Yes` and set `slow_connection_wait_seconds` to the appropriated wait time (in seconds), this will pause the execution between test steps  
```ini
slow_connection=No
slow_connection_wait_seconds=10
```



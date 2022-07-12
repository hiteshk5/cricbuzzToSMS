# cricbuzzToSMS

*cricbuzzToSMS* is a program that scrapes live match details from CricBuzz using *Selenium* and sends it as an SMS using *Fast2SMS API* 

## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.

```bash
pip install selenium
```
2. Install the firefox geckodriver.
You can follow [this guide](https://dev.to/eugenedorfling/installing-the-firefox-web-driver-on-linux-for-selenium-d45) for installation on Linux. Guides for Windows and Mac are available on the internet.

3. Clone the repo on your computer 

## Usage
1. Create an account on [Fast2SMS](www.fast2sms.com). 
2. In DEV API section, copy the API Key. Example API key is :
```bash
"weBQKBrtZzLnD2ZUEnUYJIO40zZGnjgZm3BA1SAUd0qZ56gHm0k3X45DWR9c" 
#Note: This key is an example key only. It will not work when trying to run the code.
```
3. Open keys.py and paste the API Key. Example
```python
API_KEY = 'weBQKBrtZzLnD2ZUEnUYJIO40zZGnjgZm3BA1SAUd0qZ56gHm0k3X45DWR9c'
```
4. Add the numbers you want to send the SMS to. Example:
```python
'numbers': '9999999999, 7777777777, 6666666666'   
```
5. **To only run the scrapper:** Run scrapper.py . This will print the scores on the terminal.
```python
python3 scrapper.py
```
6. **To run scrapper + send SMS:** Run main.py
```python
python3 main.py
```
 ## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

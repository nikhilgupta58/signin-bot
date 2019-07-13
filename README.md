# Sign-in Bot

Sign Bot is a python program that can retrieve the password and can sign you in any portal.

## Installation

You need to have Python3 or above version.
A python library "selenium"
```bash
pip install selenium
```
As this is particularly designed for chrome browser then you need to install [chromedriver](http://chromedriver.chromium.org/downloads) and save it in the location where chrome.exe has been saved.

## Usage

Get the element name using inspect element of that portal and replace it with
```
element_for_submit = "btnSubmit"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# TODO:
 - improve area filter in the feed:
   - subito Roma
   - immobiliare Roma
   - soloAffiti Roma
   - casaIT Bari
   - idealista Bari
   - subito Bari
   - immobiliare Bari
   - soloAffiti Bari
 - parse existing file to csv
 - get csv file on G MyMaps
 make scraper work for the rest of the websites
 xPaths could go in config.json


- https://radar.com/ api to calculate distance to metro
- energetic_class '//span[@class="chars__ec__class--value"]'
- reference '//div[@class="grid-item tp-s--x2s c-txt--f5 grid-item"]'
- consider clicking on main image and extract images
- GMAPS:
   - https://www.google.com/earth/outreach/learn/visualize-your-data-on-a-custom-map-using-google-my-maps/
   - https://stackoverflow.com/questions/50313126/google-maps-api-search-for-nearest-train-station
- alternative: mapbox https://labs.mapbox.com/education/impact-tools/sheet-mapper/




# House Search

For this to work, turn on **2-Step Verification** on your email provider and get an
app-specific password.
Create a `.env` file on your project's root directory with the following 
structure:
```
EMAIL_ADDRESS=<your email>
EMAIL_PASSWORD=<your password>
```

## Dependencies
Install the dependencies using the [requirements](requirements.txt) file, or individually:
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)



## Sources:
- [Reading emails with python](https://www.thepythoncode.com/article/reading-emails-in-python)
- [imaplib package](https://docs.python.org/3/library/imaplib.html)
- [Regex](https://www.geeksforgeeks.org/pattern-matching-python-regex)
- [Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)
- [XPath Syntax](https://www.w3schools.com/xml/xpath_syntax.asp)

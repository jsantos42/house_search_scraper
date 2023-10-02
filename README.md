# House Search Scraper
I wrote this scraper for when I was desperately looking for a house in Rome.
The idea was to make it ready for all the big Italian housing ad websites
([Subito](https://www.subito.it/), [Immobiliare](https://www.immobiliare.it/),
[SoloAffitti](https://www.soloaffitti.it/), [Casa](https://www.casa.it/)
and [Idealista](https://www.idealista.it/)), but currently it only supports
[Casa](https://www.casa.it/) (I ended up finding a house and no longer 
needed to tweak the program!).

## Setup
1. Go to the pretended housing ad website and signup for their email alerts.
2. Turn on **2-Step Verification** on your email provider and get an 
app-specific password.
3. Create a `.env` file on your project's root directory with the following
structure:
```
EMAIL_ADDRESS=<your email>
EMAIL_PASSWORD=<your password>
```
4. Install the dependencies using the [requirements](requirements.txt) file.
5. Run the scraper!



###  TODO:
 - add energetic_class `//span[@class="chars__ec__class--value"]`
 - add reference `//div[@class="grid-item tp-s--x2s c-txt--f5 grid-item"]`
 - xPaths could go in config.json
 - make scraper work for the rest of the websites
 - map the houses (eg: using [Mapbox](https://labs.mapbox.com/education/impact-tools/sheet-mapper/))
 - calculate distance to subway stations (using [Radar](https://radar.com/) or 
GMaps [here](https://www.google.com/earth/outreach/learn/visualize-your-data-on-a-custom-map-using-google-my-maps/)
and [here](https://stackoverflow.com/questions/50313126/google-maps-api-search-for-nearest-train-station))


### Dependencies
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)


### Sources:
- [Reading emails with python](https://www.thepythoncode.com/article/reading-emails-in-python)
- [imaplib package](https://docs.python.org/3/library/imaplib.html)
- [Regex](https://www.geeksforgeeks.org/pattern-matching-python-regex)
- [Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)
- [XPath Syntax](https://www.w3schools.com/xml/xpath_syntax.asp)

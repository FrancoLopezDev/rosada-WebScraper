# Rosada Webscraper

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a web-scraper I built for a PhD candidate during my sophomore year of college to help him gather data for his graduate thesis. The program was written in Python, and uses [Selenium](https://www.selenium.dev/) to automate the selection of drop down menus, click on links, and then scrape data from the website to write to a CSV file. 

Website: http://siops.datasus.gov.br/filtro_rel_ges_covid_municipal.php

I named the project "Rosada" after [Rosey](https://thejetsons.fandom.com/wiki/Rosey) the robot in *The Jetsons*. In the TV show, Rosey helps the family by doing monotonous chores such as cleaning. This bot was my attempt to help the PhD student and his undergraduate assistants save a bunch of time gathering all of the data by hand. 

This was one of the first "real" projects I had ever done, so the code looks pretty terrible. However, it got the job done. Because I am not expecting anyone else to ever use/need the code, I've decided to stop development for now. Maybe one day in the future I'll come back and clean it up. 

If you like my work please consider donating:

<a href="https://www.buymeacoffee.com/seaborg1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Getting Started

These are some basic instructions to help you get started.

### Prerequisites

What you need to install:

*  [Selenium](https://www.selenium.dev/) - Tool for automating web applications
* [ChromeDriver](https://chromedriver.chromium.org/getting-started) - Allow automation through Chrome Desktop

The ChromeDriver is an executable file that is downloaded to your local machine. 

### Installing

A step by step series of examples that tell you how to get everything running

Install selenium

```html
pip install selenium
```

Set the path to the ChromeDriver (example)

```python
path = '/Users/admin/desktop/rosada/chromedriver'
```

Change the permissions for ChromeDriver (change with the correct path)

```html
chmod +x /Users/admin/desktop/rosada/chromedriver
```

### Usage

To run the program simply open your Terminal and go to the directory in which the files are located.

Then run:

```html
python3 rosada.py
```

This starts the program. For every 1000 pieces of data collected, the program will output that current number to the terminal. Press Ctrl + C at any time to terminate the program. If the program is left to run, then it will print "I'm all done!" when it completes

## Built With

*  [Selenium](https://www.selenium.dev/) - Tool for automating web applications
* [ChromeDriver](https://chromedriver.chromium.org/getting-started) - Allow automation through Chrome Desktop
* [Python](https://www.python.org/) - Language of the gods

## Contributing

Please read [CONTRIBUTING.md](https://github.com/seaborg1/rosada-WebScraper/blob/main/CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests to us. Follow the general guidelines outlined in the link. 

## Author

**Franco (Seaborg1)** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/seaborg1/rosada-WebScraper/blob/main/LICENSE.md) file for details

## Acknowledgments

- The PhD student writing a graduate thesis
	- Once his research is published I'll post a link to it here
- [ThoughtWorks](https://www.thoughtworks.com/en-us) - For putting together the awesome [Selenium](https://www.selenium.dev/history/) software
* Shoutout to [PurpleBooth](https://gist.github.com/PurpleBooth) - for putting this README template together

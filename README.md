# Simple Survey Form with CSS Grid

## About

This survey form project is based on FreeCodeCamp's (FCC) Responsive Web Design Certification curriculum. The  html/css requirements were written as user stories and can be found in the project's page ([here](https://learn.freecodecamp.org/responsive-web-design/responsive-web-design-projects/build-a-survey-form/)).

You can also find my CodePen to this project over [here](https://codepen.io/adriaanbd/full/pQRqrq/), which is nice because it gives you something to look at, with the option of viewing the code side by side (click on Change View at the top right).

In addition, I've included my own User Interface tests by using Python and both the Selenium and Unittest libraries. These tests are modeled on FCC's user story requirements, although it wasn't required by FCC, since they have their own automated test suite with a GUI, which you can find [here](https://codepen.io/freeCodeCamp/pen/MJjpwO), to make sure one passes all the requirements for a specific project. The reason I did this is simple: a good developer tests their code, and I want to get better at testing. Learn by doing, right?

## Testing

I used the page object model, which is a popular design pattern for web automation testing. If you're interested, you can read more about it [here](https://selenium-python.readthedocs.io/page-objects.html). Its the first time I've ever tried this, so I'm conscious it needs refactoring to eliminate repetition. Any help or feedback would be greatly appreciated.

## Requirements

To view the static survey, you just need your browser. But you could also just take a look at the CodePen I provided above.

If you'd like to take the UI test for a run, you'd need to have Firefox browser, Python 3.6+ and the Selenium library. To get Selenium just run `pip install selenium` from your command line. Then inside the working directory were you have these files, run the `ui_test.py` with Python, i.e. `python ui_test.py`.

## Feedback / Contributions

All feedback/contributions are welcome. Please submit a ticket/issue. I'd really like to refactor the test files, as there is a lot of repetition that could be avoided. This is definitely in my bucket list, although I have to keep on going with the rest of the FCC projects (next one up is a Product Landing Page).
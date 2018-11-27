# Simple Survey Form with CSS Grid

## About

This survey form project is based on FreeCodeCamp's (FCC) Responsive Web Design Certification curriculum. The  html/css requirements were written as user stories and can be found in the project's page [here](https://learn.freecodecamp.org/responsive-web-design/responsive-web-design-projects/build-a-survey-form/).You can also find my CodePen to this project over [here](https://codepen.io/adriaanbd/full/pQRqrq/)

In addition, I've used Python's Flask web framework for this project. Please
check the `requirements.txt` file for information on what you'll need.

The user interface test is modeled using the above-mentioned user requirements.
It was done using both `selenium` and `unittest` libraries. For selenium, I've
used the page object design pattern, separating the location of the web
elements (located either by id, css selector, tag name) on the `locators.py`
file, and the page method actions using those web elements on `page.py`.

## Here's a snippet of the Survey Form

![Snippet of Survey Form](https://github.com/adriaanbd/simple_survey_form/blob/master/resources/survey_form.PNG "Snippet of Survey Form")

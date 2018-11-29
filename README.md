# Simple Survey Form with CSS Grid

## About

This project was created with the following ideas:

1. Comply with the HTML/CSS requirements set forth by the *Build a
   Survey Form* project, which is the second project out of five, from
   [FreeCodeCamp](https://www.freecodecamp.org/)'s (FCC) [Responsive Web Design
   Certification](https://learn.freecodecamp.org/responsive-web-design/responsive-web-design-projects),
   which can be found
   [here](https://learn.freecodecamp.org/responsive-web-design/responsive-web-design-projects/build-a-survey-form/).
   The strict HTML/CSS version of this project can be found in my CodePen [here](https://codepen.io/adriaanbd/full/pQRqrq/).

2. Build the Back End to the Survey Form.

3. Build a User Interface test, which would validate that the main html requirements
   set forth by FCC are maintained throughout.

## Purpose

The purpose of this project is to experience horizontal development, integrating all layers of the
project:

* The user interface (HTML/CSS),
* Middleware (Flask), and
* Database (to be determined).

## Why would you fork this, use this and/or take a look at this

1. You're going through FCC's Front End Projects, or any other similar
   undertaking, but would like to experience small building blocks of full
   stack development, particularly using Python for the Back End. Note that FCC
   is heavily focused on JavaScript, which you'll still need for the Front End,
   but not necesarily for the Back End.

2. You're an employer looking at this repo.

In both of these cases, please take a look at how the project evolved, from the
initial committ consisting of the static html/css page, to what it is now.

## How would you run this locally

1. This project was done with Python 3.7.

2. Clone this repository locally. This is done by typing `git clone
   https://github.com/adriaanbd/simple_survey_form simple-survey` in your terminal.

3. I'd recommend setting up a virtual environment, which is an isolated python
   environment in your chosen directory. Do this with `python venv myvenv` in
   your terminal. This will create a virtual environment called `myvenv`. If
   you have other version of Python installed, you'd need to make sure that you
   are accessing the desired `python` when typing that term. You can check this
   out by typing `python --version`. If it says 3.7, you're good to go. If not,
   type `py --version`, which should display 3.7 if you installed it
   succesfully. If so, then you'd need to setup your virtual environment with
   the following comman `py venv myvenv`.

4. Install all requirements. In your local directory where you cloned the repo,
   type `pip install -r requirements.txt` in your terminal.

5. If you'd like to run the User Interaface tests, since I used the Firefox
   driver, you'd need to have Firefox installed, and the geckodriver on which
   Selenium relies on to use Firefox. You can get geckodriver
   [here](https://github.com/mozilla/geckodriver/releases). Make sure it's in
   your PATH. If you're having problems with Selenium, make sure to refer to [this
   page](https://selenium-python.readthedocs.io/installation.html), making sure
   everything's installed correctly.

## Starting the server locally to interact with the Survey Form

1. In your terminal, type `flask run`
2. Either click on the link provided in your terminal `http://127.0.0.1:5000/`
   or insert it directly on your web browser.

## Running the User Interface tests

1. Make sure your local server is running.
2. In the terminal, type `python -m unittest`
3. Alternatively, you can run the file directly, typing: `python tests/test_survey_ui.py`

## How does the User Interface tests work

I've used the page object design pattern, separating the location of the web
elements (located either by id, css selector, tag name) on the `locators.py`
file, the page method actions using those web elements on `page.py`, and the
tests themselves on `test_survey_ui.py`. Feel
free to look at them. The idea behind this separation, is that if something
changes to the html or css, the locators would only need to be updated in one
place.

## Further notes

Back end development is still on going, as I'm exploring adding database
functionality to store survey votes. Furthermore, there are a few more tests
that need to be added, specifically testing the GET and POST, and considering changing
the testing over to pytest.

Nevertheless, development will carry on in the `develop` branch and the
`master` branch will only be updated if all tests pass.

## Here's a snippet of the Survey Form

![Snippet of Survey Form](https://github.com/adriaanbd/simple_survey_form/blob/master/resources/survey_form.PNG "Snippet of Survey Form")

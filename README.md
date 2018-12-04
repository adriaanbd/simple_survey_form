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
* Database (SQLite).

## Getting started

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

4. If you're using a Bash terminal, activate your virtual environment with `source
   venv/myvenv/activate`. If it doesn't work for you, please Google it online.
   There are plenty of resources available.

5. Install all requirements. In your local directory where you cloned the repo,
   type `pip install -r requirements.txt` in your terminal.

## Set up the database

1. From the terminal, run the command `flask db init`

2. You should see a `migrations` folder in your root directory.

3. Migrate your db by running `flask db migrate`

4. You should see some new files in your `/migrations` folder

5. Make the db setup permanent by running `flask db upgrade`

## Play with your database to check everything's alright

1. From your terminal, run `flask shell`

2. This will load all configuration values with access to the db model.

3. Enter and check the following:

```
>>> Voter.query.all()
[]
>>> v = Voter(name="John Doe", email="john@doe.com")
>>> v
<Voter John Doe>
>>> db.session.add(v)
>>> db.session.commit()
>>> a = Answer(age=31, gender='Male', path='Full Stack', voter=v)
>>> a
<Answer (31, 'Male', 'Full Stack')>
>>> a.voter
<Voter John Doe>
>>> db.session.add(a)
>>> db.session.commit()
>>> l = Language(language='Python', voter=v)
>>> l.language, l.voter
('Python', <Voter John Doe>)
>>> db.session.add(l)
>>> db.session.commit()
>>> c = Comment(comment='I love to code', voter=v)
>>> c.comment, c.voter
('I love to code', <Voter John Doe>)
>>> db.session.add(c)
>>> db.session.commit()
```

## Starting the server locally to interact with the Survey Form

1. In your terminal, type `flask run`

2. Either click on the link provided in your terminal `http://127.0.0.1:5000/`

   or insert it directly on your web browser.

## Fill and submit the form

1. Fill all the values in the form

2. Name and email are required values

3. Click on submit, at which point you *should* receive a "Your form was submitted" message in red.

## Check your db again to check that it received the values from the form

1. `flask shell`

2. Run the following and check that the output is the same as the values you entered in the form.

```
>>>Voter.query.all()
>>>Answer.query.all()
>>>Language.query.all()
>>>Comment.query.all()
```

## Running the User Interface tests (this hasn't been thoroughly tested with db)

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

Development is still in progress:

* Unittest will be replaced by pytest.
* More tests will be added.

## Here's a snippet of the Survey Form

![Snippet of Survey Form](https://github.com/adriaanbd/simple_survey_form/blob/master/resources/survey_form.PNG "Snippet of Survey Form")

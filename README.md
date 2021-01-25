# big5 personality random data generator
Randomly generated Big 5 personality test results

Using jupyter-lab to experiment with the results. All necessary files are inside
`src/` folder. Invoke jupyter-lab by typing `jupyter-lab` after setting up the
environment.

### Usage

Install virtual environment for python, then install the packages from the
requirements file in the repo. The following commands are for macos and linux,
for windows it might be different. e.g. sometimes you have to do `python -m
virtualenv venv` instead of the first command from below.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ jupyter-lab
```

### Research Questions
Possible research questions.

- Can we create a virtual simulation to test out how well do our simulated
  entities in teams if they have a given trait score? 

### Tasks
Create your own branch and work off them.

The following tasks are for main:
- Clean up the evaluator() function.
- Add database functionalities to evaluator. Use SQLAlchemy.

# Authors
- Sirvan Almasi
- Iskander Fakhritdinov
- Matthew Shorvon

# Note:

To easily validate the data from the input json file, I used the "jsonschema" library. If you don't want to use any library, just delete the _validate() and _json_schema() methods of the classes:

**./model/car.py**
**./model/rental.py**

## Bootstrapping

Create a virtual environment and install the dependencies (jsonshcema):

```pip install -r requirements.txt```

## Test a level
From the command line:

```python -m unittest discover tests```

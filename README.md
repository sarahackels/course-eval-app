# course-eval-app
This app will use the course evaluations from Georgetown to create a dashboard for students who are deciding what class to take.

## Setup
Create and activate a virtual environment:

```sh
    conda create -n eval-env python=3.10
    
    conda activate eval-env
``` 

```sh
    pip install -r requirements.txt
```

Obtain an API Key from Google Cloud API (https://console.cloud.google.com/apis/api/sheets.googleapis.com). Or ask Sarah Ackels saa390@georgetown.edu

Download your API key from Google Cloud as a JSON file and name it "your-google-credentials.json"

In terminal, run 
```sh
    cat your-google-credentials.json | base64
```

Copy the resulting string - this is your GOOGLE_CREDENTIALS secret.

Obtain Google Sheets ID for data file (DOCUMENT_ID) from Sarah Ackels saa390@georgetown.edu

Create a ".env" file and paste in the following contents:

```sh
    GOOGLE_CREDENTIALS="______"
    DOCUMENT_ID="______"
```
## Use
Get the data into the environment:
```sh
    python app/get_data_online.py
```

Search for results about a professor:
```sh
    python app/search_prof.py
```

Search for results about a course:
```sh
    python app/search_class.py
```

Get list of all professors at Georgetown:
```sh
    python app/all_professors.py
```
Get list of all courses at Georgetown:
```sh
    python app/all_classes.py
```

## Live Website
This is actively running on https://course-eval-app.onrender.com

## Testing
Run tests:
```sh
    pytest
```

## Web App

Run the web app (then view in the browser at http://localhost:5000/):


### Mac OS:

```sh
    FLASK_APP=web_app flask run
```

### Windows OS:

```sh
    export FLASK_APP=web_app
    flask run
```
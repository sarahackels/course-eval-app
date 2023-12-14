# course-eval-app
This app will use the course evaluations from Georgetown to create a dashboard for students who are deciding what class to take.

## Setup
Create and activate a virstual environemenmt:

```sh
    conda create -n eval-env python=3.10
    
    conda activate eval-env
``` 

```sh
    pip install -r requirements.txt
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

## Testing
Run tests:
```sh
    pytest
```
# DatabaseLess ToDo API

Just inspiring by this tweet to make some API Services without database, in this case i am using in memory state
So the data will be destroyed if the server restart/shutdown.


## Setup Python Environment

```python3 -m venv venv```

then activated it

```source venv/bin/activate```

Install the requirements file

```pip install -r requirements.txt```

## Run

```uvicorn src.main:app --port 8000```


# DatabaseLess ToDo API

Just inspiring by [this tweet](https://twitter.com/lynxluna/status/1401470901133090816?s=21) to make some API Services without database, in this case i am using in memory state

So the data will be destroyed if the server restart/shutdown.


## Setup Python Environment

```python3 -m venv venv```

then activated it

```source venv/bin/activate```

Install the requirements file

```pip install -r requirements.txt```

## Run

```uvicorn src.main:app --port 8000```


## AWS Lambda Deployment with Serverless Framework

### Install serverless

```
npm install -f serverless
```

### Install serverless plugins

```
npm install
```

### Run the deployment command

Change the params with your own configurations

region: the aws region
aws-profile: your aws profile configured (unset: default)
iamrole: Execution Role ([read how to create it](https://github.com/dwisulfahnur/databaseless-api/wiki/Create-Lambda-Execution-Role))


```
serverless deploy --region 'ap-southeast-1' --stage 'dev' --aws-profile 'sbrg' --iamrole 'arn:aws:iam::XXXXXXXXXXX:role/LambdaExecutionRole'
```


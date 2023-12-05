# EQW

I don't know what this acronym means, but it is a training program for analyzing network traffic for vulnerabilities

## Launch
- Clone project:
```
$ git clone https://github.com/iamcrysun/eqw.git
```
- Make a virtual env
```
$ cd eqw
$ python3 -m venv venv
$ source venv/bin/activate
```
- Install requirements
```
$ pip install -r requirements.txt
```
- Launch server:
```
$ python3 server/src/run.py
```
It will run an uvicorn server with a FastAPI app 
- Launch client:
```
$ python3 desktop/main.py
```
It will start a tkinter app

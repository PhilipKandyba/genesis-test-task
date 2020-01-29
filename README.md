# genesis-test-task

This is a test task for AQA position


## How to setup test project

>Before you start the test you need to set up credential for testing stage in ```src/config.py```

### First way
  You can use a Makefile. Call next command for setup:
```
make setup
```
This command:
 - Setup virtual environment in directory
 - Install all dependencies 
 - Downloads last chromedriver
    
After that you can run the test session:
```
make run
```

### Second way
You can setup all yourself:
 - Install all dependencies from requirement.txt
 - Put chromedriver in ops directory
 - Run test session with command:  ```pytest run```

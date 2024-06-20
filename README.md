[![CI](https://github.com/niikun/function_from_zero/actions/workflows/main.yml/badge.svg)](https://github.com/niikun/function_from_zero/actions/workflows/main.yml)

# function_from_zero
function_from_zero


## Step 1: Configure Development environment

* Configure Github Codespaces or equivalent(Cloud9 etc)
* Create scaffold for structure of project: "Makefile","requirements.txt"
* Optional (setup virtualenv)

## Step 2: Get interactive debugging working

* Use IPython and ipdb

```python
x = 1
y = 2
import ipdb; ipdb.set_trace()
print(x+y)
```

## Step 3: Build container

`docker build .` 
`docker image ls`

Run container
something like this

`docker run -p 127.0.0.1:8080:8080 a81ce4f35866`


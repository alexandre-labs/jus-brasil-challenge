# Jus Brasil - Backend Engineer Challenge

The challenge description is available in the dir. `docs`.

## Badges

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)


## Solution

I used the challenge as an opportunity to learn more about asyncio and its
 ecosystem. It's fun and challenging, but a good approach (so far) to a solution
based on IO bound.

The code organization is really simple. As you can see in the commit history,
I did start trying an approach using more modules, but at the end I could
simplify it a bit and reuse the main parts.

The challenge ask for an API to query processes in the courts TJSP and TJMS. So,
the application has only two endpoints.

## Endpoints

The first endpoint is `/query` and thank to FastAPI the API gives a `/docs`
endpoint, where we can try the API and based on types (Pydantic) access all the
schemas (contracts) defined by the application.

## Performance

This is not a complete or really detailed approach, but I would like to share
a real test.

### Scenario

* Network: My connection is `Claro 4g Max`.
* I use the tool `hey` with its default settings.
* I also use `gunicorn` as process manager
* Process numberer : `1000356-42.2019.8.26.0218`. I choose this one because it
 would require executing queries in the three jurisdiction.

```bash
 ~> ./hey -m POST -d '{"process_number": "1000356-42.2019.8.26.0218","process_court":"TJSP"}' http://0.0.0.0:8000/query

Summary:
  Total:        17.3001 secs
  Slowest:      5.5434 secs
  Fastest:      1.8597 secs
  Average:      4.0176 secs
  Requests/sec: 11.5606

  Total data:   2261600 bytes
  Size/request: 11308 bytes

Response time histogram:
  1.860 [1]     |■
  2.228 [2]     |■■
  2.596 [3]     |■■■
  2.965 [6]     |■■■■■■■
  3.333 [29]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  3.702 [36]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  4.070 [31]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  4.438 [19]    |■■■■■■■■■■■■■■■■■■■■■
  4.807 [28]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  5.175 [29]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  5.543 [16]    |■■■■■■■■■■■■■■■■■■


Latency distribution:
  10% in 3.0511 secs
  25% in 3.5232 secs
  50% in 3.8145 secs
  75% in 4.6659 secs
  90% in 5.0775 secs
  95% in 5.1939 secs
  99% in 5.5428 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0005 secs, 1.8597 secs, 5.5434 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.0001 secs, 0.0000 secs, 0.0050 secs
  resp wait:    4.0170 secs, 1.8597 secs, 5.5421 secs
  resp read:    0.0000 secs, 0.0000 secs, 0.0002 secs

Status code distribution:
  [200] 200 responses

```

### Stack

#### Web framework

I did choose FastAPI  Some time ago, I asked the community how to introduce the
 framework to my teammates, and I think that answer gives a good idea about
 "Why to use FastAPI ?":

```
@alexandre my suggestion would be to add a small layer of FastAPI on top of
 what you have, like a /api/v2/ that is handled by FastAPI.

Then start migrating little pieces. Just use normal def functions, it will be
 easier for your team to adopt on one side, on the other, most of the current
 databases don't support async, so, you would still have to use normal def.

You can get the request directly, and in some cases that's necessary.
 But you'll probably end up finding the advantages of declaring most of the parameters with types.

In short, you can use FastAPI as a normal common framework, that's the easiest
 to adopt, but then you can start playing with the additional features and see
 how they help a lot the process.

About learning curve, it was designed from the beginning to be very easy to
 understand and use, for each feature there's been a lot of consideration,
 to make it as simple to use and intuitive as possible.
 But all keeping the maximum flexibility.

It is all based on autocomplete, so, in many cases, you can just trigger the
 completion in your editor and find what you were looking for.

Also, the docs are designed/written to gradually teach all the parts easily,
 even including explanations of more "advanced" features of Python.
 I thought a lot about new developers while creating the docs, so, it should be
 very easy for experienced developers.
```

#### Tools

* Pre-commit and Black for code formatting;
* Poetry for dependency management and packaging;
* Flake8 and MyPy as linters; and
* Vim

## Setup

As my first task in the project, I tried to define a simple way to install,
 run the tests and execute the application.

### Installation

* Create your own virtualenv (e.g. virtualenvwrapper) and run `make install`

* Install it using docker from the command `make dbuild`

### Running the service

* Run it inside the virtualenv: `make run-dev`
* Run it inside a docker container `make drun`

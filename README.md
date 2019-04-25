## TempMessenger
### Goals
* A user can go to a website and messages.
* A user can see messages that others have sent.
* Messages automatically expire after a configurable amount of time.

## Requirements
* Nameko microservices framework for Python
* Docker

##### Starting a RabbitMQ container
 In the terminal execute:
  $ `docker run -d -p 5672:5672 -p 15671:15672 --name rabbitmq rabbitmq `

##### Initial Setup
While from the root directory.
To generate nameko dependencies file:

 $ `pip-compile requirements/base.in`

To generate pytest dependencies file:

 $ `pip-compile requirements/test.in `

To install the required packages for our development environment:

$ `pip install -r requirements/base.txt -r requirements/test.txt `

###worklow

Used [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) for versioning.

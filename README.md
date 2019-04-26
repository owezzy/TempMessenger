## TempMessenger
### Goals
* A user can go to a website and messages.
* A user can see messages that others have sent.
* Messages automatically expire after a configurable amount of time.

## Requirements
* Nameko microservices framework for Python
* Docker

##### Starting a RabbitMQ container
* It is good practice when running services in containers, Use an isolated docker network in order to be able to reference it using DNS.
 
  `docker network create nameko_net`

 In the terminal execute:
 
  $ ` docker run -d --network nameko_net --hostname rabbitmqhost --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management`

##### Starting a Redis Container
* Redis is an in-memory data store
* Execute this in terminal: 

  $ ` docker run -d --network nameko_net --hostname redishost -p 6379:6379 --name redis redis`
* Port 6379 is exposed on the container to facilitate communicate between Nameko and Redis container
##### Installing Python Redis Client
* This allows interaction with Python 
* Add redis in the `base.in` file, and recomplie using `pip-compile requirements/base.in` to generate it to new `base.txt`.

##### Initial Setup
While from the root directory.
To generate nameko dependencies file:

 $ `pip-compile requirements/base.in`

To generate pytest dependencies file:

 $ `pip-compile requirements/test.in `

To install the required packages for our development environment:

$ `pip install -r requirements/base.txt -r requirements/test.txt `

### worklow

Used [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) for versioning.

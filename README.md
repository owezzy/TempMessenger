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
> docker run -d -p 5672:5672 -p 15671:15672 --name rabbitmq rabbitmq

###worklow

Used [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) for versioning.

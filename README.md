# uplight-coding-challenge

This is this coding challenge for submission to Uplight.

## Instructions for use

Clone the repo locally using `git clone https://github.com/logknees/uplight-coding-challenge.git`, or download the repo as a .zip file.

Then, in the root directory of the project, type into your terminal the command `make start` to build the images if they don't yet exist, and turn on the containers.

You can also use the command `make run` in order to start the containers once the images are built.

Finally, use the command `make serve` to test if the api is running.

Voila! You can now test the api! 
Accepted requests:
`GET localhost:56733/`
`GET localhost:56733/token`
`POST localhost:56733/token` 

The POST requests should have at least one key/value pair in the request body, or the api will throw a `400 bad request`. This is by design, although we could have easily had an empty request also return just the signature.

Use `make stop` to turn off the containers.

Try `make test` to run automatic HTTP request tests.

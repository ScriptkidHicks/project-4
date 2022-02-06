# UOCIS322 - Project 4 #
You'll learn how to write test cases and test your code, along with more JQuery.

## Overview

You will reimplement RUSA ACP controle time calculator with Flask and AJAX.
> That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

### ACP controle times

This project consists of a web application that is based on RUSA's online calculator. The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly. 

We are essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data. 

## Downloading and use

To download this product, fork the repo, then clone it to your local machine. To run it, you can either generate a virtual environment using virtualenv, and the requirements file contained in this repo, or you can run it by building and running a docker image. If you are using the venv option, use the following command to start the machine:

```
./backstart.sh
```

Otherwise, if you are using the docker approach, you can build the docker image with the following commands:

```
cd brevets
docker build .
docker run {your image id goes here}
```

once it's running, the machine will provide some logging info about the port you are exposing it on. You should create a credentials.ini copied from the credentials skeleton here provided. If you don't, the container will default to the defualt ini. In the loggin info on first startup, the machine will register the ip adress, and port it is running on. Visit that port to begin interacting with the brevets time calculator.

## using the calculator

To use the brevets calculator, update the distance of the brevet you would like, set the starting time of the brevet (this will autopopulate with the current time and date) and begin entering control distances. Notable, the site will not let you enter distance that are longer than 120% of the total brevet distance. Additionally, if you attempt to enter a negative number, the page will correct your mistake by setting the distance to 0.

## The logic of the calculator

If the distance is 0, then the opening time will be the opening time of the whole brevet, and the closing time will be an hour therafter. If the control is any other distance, then the total distance of that control will be divided by the relevant maximum and minimum speeds to provide the opening and closing times of that control. Note that while placing a control at 0 distance will result in a closing time an hour after the opening time of the race, any distance under 15km will not offer such a courtesy, and will result in a closing time before the closing time of the start of the race. It is advised that one does not do so, as a result.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.

Completed by Tammas Hicks

# Covid 19 Early detection

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Dependency Status](http://img.shields.io/gemnasium/badges/badgerbadgerbadger.svg?style=flat-square)](https://gemnasium.com/badges/badgerbadgerbadger) [![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger)[![Gem Version](http://img.shields.io/gem/v/badgerbadgerbadger.svg?style=flat-square)](https://rubygems.org/gems/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/Gauravsahadev/Covid-19-Early-detection/blob/master/LICENSE) [![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)

With the continuous increase in the number of Covid-19 positive patients and suspects, it is becoming difficult for the clinicians to detect patients after taking their clinical tests. The current tests are mostly based on reverse transcription polymerase chain reaction (RT-PCR). It takes 4–6 hours to obtain results, which is a long time compared with the rapid spreading rate of COVID-19. Also, RT-PCR test kits are in huge shortage.

Here, we have come up with a solution to this problem. We have prepared a Web Application using which the early detection of Covid can be done.
The dataset has been taken from [here ](https://github.com/ieee8023/covid-chestxray-dataset)  , it contains chest X-rays of various patients. The model has been trained using tensorflow.

Please, go and check our simple WebApp :desktop_computer: [Covid-19 Early detection](http://covid19-early-detection.herokuapp.com/).

![Index page](https://github.com/Gauravsahadev/Covid-19-Early-detection/blob/master/app/static/img/img1.png)
![Prediction page](https://github.com/Gauravsahadev/Covid-19-Early-detection/blob/master/app/static/img/img2.png)
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Clone the repo 
```
git clone https://github.com/Gauravsahadev/Covid-19-Early-detection.git && cd Covid-19-Early-detection/
```
What things you need to install
* Python3
```
sudo apt install python3 python3-pip
```
* Dependencies
```
pip3 install -r requirements.txt
```
### Installing

A step by step series of examples that tell you how to get a development env running

Inside dir
```
export FLASK_APP=run.py
```

And repeat
```
export FLASK_ENV=development
```
Run Flask app
```
flask run
```
Go to [127.0.0.1:5000](127.0.0.1:5000), You will see APP Running

## Built With

* [Flask](https://g.co/kgs/bDNDHj) - The web framework used
* [Tensorflow](https://g.co/kgs/kXV43E) - Open Source ML library

<!-- ## Contributing

Please read for details on our code of conduct, and the process for submitting pull requests to us. -->
 

## Authors

*  :man_technologist: - [Gaurav Sahadev](https://github.com/Gauravsahadev)
*  :girl: - [Debanjona Bhattacharjya](https://github.com/DEBANJANAB)

If you like our endeavour, Please give a :star:


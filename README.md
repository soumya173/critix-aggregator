<p align="left"> <img src="https://img.shields.io/github/issues-pr-raw/soumya173/critix-aggregator" alt="open-pull-requests" /> <img src="https://img.shields.io/github/issues/soumya173/critix-aggregator" alt="open-pull-requests" /></p>
# Table of contents
* [General info](#introduction)
* [Technologies](#technologies)
* [Setup](#project-setup)
* [Design](#design)

## Introduction
A movie review aggregator site, this would collect and aggregate data from different websites and provide a all-in-one place to search for movie reviews

## Technologies:
  - Back end
    + Django (https://www.djangoproject.com/)
  - Databse
    + MySQL? MongoDB?
  - Front end
    + Bootstrap 5 (https://getbootstrap.com/)
    + jQuery
    + Should we explore angular?

## Project Setup
### Create a virtual dev environment and activate it
```
python3 -m venv venv-critix
source venv-critix/bin/activate
```
### Install the required packages
```
pip3 install -r requirements.txt
```
### Migrate the db changes
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### Start the local Django server
```
python3 manage.py runserver
```

## Initial Plan
### Sites in consideration
  - https://www.imdb.com/
  - https://www.rottentomatoes.com/
  - https://www.metacritic.com/


## Design:
  + General
    + No user authentication (except admin panel)
    + Home page to show recent / latest movies 
    + Each movie should have it's own page with details about movies and reviews from users
    + Search / filter movies by {name, ratings, release year etc}. This can be decided after the database is design (parameters to be collected for each movie) is finalized
  + Configurator
    + Admin will configure 
      + which sites to consider while scrapping data
      + a list of movies to get the information from the configured sites
    + A background process? or trigger? or scheduled task?
      + parse the pre-configured sites for dumping the movie data in the db
      + Check if we have APIs to collect data instead of web-scrapping

![critic](https://user-images.githubusercontent.com/31511160/122633737-aba2ba00-d0f7-11eb-8012-3d21823bf2fa.jpg)

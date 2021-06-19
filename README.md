# critix-aggregator
A movie review aggregator site, this would collect and aggregate data from different websites and provide a all-in-one place to search for movie reviews

# Initial Plan
## Tech Stack:
  - Back end
    + Django (https://www.djangoproject.com/)
  - Databse
    + MySQL
  - Front end
    + Bootstrap 5 (https://getbootstrap.com/)
    + jQuery
    + Should we explore angular? Or Nodejs?

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

![critic](https://user-images.githubusercontent.com/31511160/122633737-aba2ba00-d0f7-11eb-8012-3d21823bf2fa.jpg)

# Click That Recommendation Button 

Authors: Jasmine Huang, Jonathan Fetterolf, Matthew Duncan, & Michael Licul

#add image logo

## Overview

We analyzed a dataset from the GroupLens research lab at the University of Minnesota (https://grouplens.org/datasets/movielens/latest/). Since we ran our analysis on a smaller cloud platform, Gradio, instead of one of the larger cloud platforms, AWS or Google Cloud, we used a smaller dataset containg 100,000 user ratings.  


## Buisness Understanding

Our team has been tasked with implementing a recommendation system for the movie rental company, RedBox. The model will provide users with the top 5, top 10, or top 20 movie recommendation based on their ratings of other movies.

We have three main goals:
- Create a recommendation system model that allows users to input movie ratings and provides movie suggestions.
- Be able to store user ratings for future recommendation requests.
- Be able to provide specific genre recommendations based on a users request.

A successfully implemented recommender system can increase customer engagement, loyalty, satisfaction, and retention. All of which lead to an increase of sales.

## Data Source 

As mentioned, that data used for this project comes from multiple datasets from the GroupLens lab at the Unversisty of Minnesota. These datasets include: 
- links.csv
- movies.csv
- ratings.csv
- tags.csv

## Exploratory Data Analysis

### links_df 
This file is a key to merge movie identifiers with IMDB Database and The Movie DataBase. We will be focusing on the MovieLens database for this analysis and will not need this file.
#add links_df head
### movies_df
This .CSV file will be very helpful for our analysis. It provides us with the title of movie in relation to its unique identifier and lets us know the genre categories that the movie would fall under.

There are 9737 unique movie titles. Repeats for 5 movies:
- Emma (1996) 2
- Saturn 3 (1980) 2
- Eros (2004) 2
- Confessions of a Dangerous Mind (2002) 2
- War of the Worlds (2005) 2

#add image with movie count genere

### ratings_df
This .CSV will be the primary datafile for this analysis. It includes relevant information including userId, rating, and movieId. timestamp is not relevant for this analysis and will be dropped. 
#add ratings_df head image

### tags_df
This .CSV could be helpful for analysis as it provides keyword insights to each of the films. timestamp will not be helpful for this analysis and will be dropped later.
#add tags_df head image
#add counts of movie tags

## Creating New DataFrame

To better understand and work with the separate files, they have been merged to one, larger working file. After cleaning the merged DataFrame, we have 100,836 reviews for 9,724 movies.

# Modeling 

We will be using the Surprise library for this analysis. This library requires that data inputs be limited to three columns of information:
- User
- Movie
- Rating

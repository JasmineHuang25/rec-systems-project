#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a place to hold commonly used functions *include doc strings please


# In[ ]:
import pandas as pd
import numpy as np


# new_user_df = pd.DataFrame
# movies_df = pd.DataFrame
# baseline = None

def new_user(new_user_df=None, movies_df=None):
    # creating a while loop so that the program runs until everything is satisfied
    new_user_cleared = False
    while new_user_cleared is False:
        # checking if new user or not
        answer = input("(Type 'quit' at any time to exit.) \n\nAre you a new user? (yes/no): ")
        new_user_cleared = False
        # this section is for new users
        if answer == 'yes':
            ok_to_move_on = False
            while ok_to_move_on is False:
                # creating a new userId based on the last one available
                new_user_id = (new_user_df['userId'].max() + 1)
                # asking for them to create a username
                username = input('Please enter a unique username: ')
                # letting them quit the program if they want to stop
                if username == 'quit':
                    print('Thank you. Closing the program.')
                    user_id = np.NaN
                    username = np.NaN
                    password = np.NaN
                    new_user_cleared = True
                    ok_to_move_on = True
                    break
                else:
                    # Checking the list of usernames to see if its available
                    user_check = len(new_user_df[new_user_df['username'] == username]) <1
                    if user_check:
                        # having them make a new password
                        password = input('Please enter a password: ')
                        # letting them quit the program if they want to stop
                        if password == 'quit':
                            print('Thank you. Closing the program.')
                            user_id = np.NaN
                            username = np.NaN
                            password = np.NaN
                            new_user_cleared = True
                            ok_to_move_on = True
                            break
                        else:
                            # creating a new account with user input username and password
                            ok_to_move_on = True
                            new_user_cleared = True
                            print('\nWelcome! Your new account is created...\n')
                            user_id = new_user_id
                    else:
                        # returns them to make a new username if the name isnt available
                        print('Sorry, that name is taken.')
        # this section is for existing users    
        elif answer == 'no':
            ok_to_move_on = False
            while ok_to_move_on is False:
                username = input('Please enter your username: ')
                # letting them quit the program if they want to stop
                if username == 'quit':
                    print('Thank you. Closing the program.')
                    user_id = np.NaN
                    username = np.NaN
                    password = np.NaN
                    new_user_cleared = True
                    ok_to_move_on = True
                    break
                else:
                    # checking to make sure username is in the list of active users
                    user_check = new_user_df[new_user_df['username'] == username]['username'] == username
                    if len(user_check.values !=0):
                        password = input('Please enter your password: ')
                        # letting them quit the program if they want to stop
                        if password == 'quit':
                            print('Thank you. Closing the program.')
                            user_id = np.NaN
                            username = np.NaN
                            password = np.NaN
                            new_user_cleared = True
                            ok_to_move_on = True
                            break
                        else:
                            # checking password match with username
                            password_check = new_user_df[(new_user_df['username'] == username) & (new_user_df['password'] == password)]['password'] == password
                            if len(password_check.values) !=0:
                                user_id = new_user_df[(new_user_df['username'] == username) & (new_user_df['password'] == password)]['userId']
                                user_id = user_id.values[0]
                                print('...\n...\nLog-in Successful.')
                                ok_to_move_on = True
                                new_user_cleared = True
                            else:
                                # letting them know that there is no username password match
                                print('Sorry, that username and password is not in the system.')
                    else:
                        # letting them know that there is no username with that name in the system
                        print('Sorry, that username is not in the system.')
        # letting the user quit if they want to stop the program
        elif answer == 'quit':
            print('Thank you. Closing the program.')
            user_id = np.NaN
            username = np.NaN
            password = np.NaN
            break
            
        elif new_user_cleared == True:
            break
        else:
            # message if a user tries to enter anything but yes or no
            print('Invalid entry. Please enter (yes/no).\n')
          
    if user_id:
        
        return user_id, username, password


# In[ ]:


#  Newest one to coordinate better with other function

def movie_recs(user_id, username, password, main_df = None, movies_df=None):
    # Setting the base rating at zero
    rating = 0
    # creating a new DF to hold the temp ratings
    current_session_df = pd.DataFrame()
    # whether or not its ok to quit the recommend prompt loop
    ok_to_quit = False

    # the loop to make recommendations
    while ok_to_quit is False:
        # prints message if they have less than 5 ratings
        if len(main_df[main_df['userId'] == user_id]) < 5:
            print("You need at least 5 reviews before we can make recommendations.")
        else:
            print('You are now ready to make additional recommendations.')
        # setting a loop to keep sampling if the sample is already in the main df or in the temp df
        ok_to_move_on = False
        while ok_to_move_on is False:
            # pulling sample from most rated moves
            top_500 =main_df.groupby('movieId').count()\
            .sort_values('userId', ascending=False).head(500)
            top_500 = top_500.reset_index()[['movieId']]
            top_500 = top_500.merge(movies_df, on='movieId', how='left')
            movie_review = top_500.sample()
            movie_check = movie_review['movieId'].values
            # checking length of df to see if its been filled yet
            # ensuring movie has not already been rated
            if len(current_session_df) != 0:
                if movie_check not in main_df[main_df['userId'] == 
                                                  user_id]['movieId'].values and\
                movie_check not in current_session_df['movieId'].values:
                    ok_to_move_on = True
                # resample if already rated
                else:
                    continue
            else:
                # ensuring movie has not already been rated
                if movie_check not in main_df[main_df['userId'] == 
                                                  user_id]['movieId'].values:
                    ok_to_move_on = True
                else:
                    # resample if already rated
                    continue
        # creating a loop to ensure that user provides a valid rating
        while rating not in range(1,6):
            # creating a dictionary to store rating info that will be appended to df
            rating_dict = {'userId':user_id, 
                       'movieId': np.nan, 
                       'rating': np.nan, 
                       'title': np.nan, 
                       'genres': np.nan, 
                       'username': username, 
                       'password': password}
            print(f"\n(Type 'quit' to stop rating movies.) \n")
            # telling user how to rate
            print(f'Please rate the movie 1-5. If you have not seen the movie, type "n" to skip: \n')
            # giving user movie info
            print(f"{movie_review['title'].values}")
            rating = input('Rating: \n')
            # letting the user quit if they dont want to rate
            if rating == 'quit':
                print('\n\nThank you for ranking movies.')
                # checking to see if the user made any ratings during this session
                if len(current_session_df) != 0:
                    print('Here are the results of your ranking session:')
                    # showing the user the ratings they made
                    print(current_session_df[['title', 'rating']])
                    # checking if user wants to save ratings
                    submit_ratings = input('\nWould you like to save these ratings to your profile? (yes/quit): ')
                    if submit_ratings == 'yes':
                        # saving ratings to main database and closing program
                        temp_df = main_df.append(current_session_df, ignore_index=True)
                        ok_to_quit = True
                        ok_to_move_on = True
                        to_return = True
                        print('\nThank you. Your results have been saved to the main system!')
                        break
                    elif submit_ratings == 'quit':
                        # not saving ratings to main database and closing program
                        rating = 10
                        ok_to_move_on = True
                        to_return = False
                        ok_to_quit = True
                        print('Thank you for trying the movie recommendor system.')
                        print('Your results have not been saved.')
                        break
                    else:
                        # user did not enter a valid input to save or quit
                        print('That is not a valid input. Please Try again.')
                else:
                    # quitting the program without saving anything if dataframe is empty
                    print('Program is now closing.')
                    ok_to_move_on = True
                    rating = 10
                    to_return = False
                    ok_to_quit = True
                    break
            # letting user skip a movie review if they havent seen it
            elif rating == 'n':
                print('\n')
                break

            else:
                try:
                    # trying to convert rating input to float
                    rating = float(rating)
                    if rating not in range(1,6):
                        # letting user know that they need to use 1-5
                        print('That is not a valid rating, please enter a value 1-5:')
                        continue
                    else:
                        # saving user rating to temp df 
                        rating_dict['movieId'] = movie_review['movieId'].values[0]
                        rating_dict['rating'] = rating
                        rating_dict['title'] = movie_review['title'].values[0]
                        rating_dict['genres'] = movie_review['genres'].values[0]
                        current_session_df = current_session_df.append(rating_dict, ignore_index=True)
                        rating = 0
                        ok_to_move_on = False
                        print('Saving rating to temporary memory...\n\n')
                        break
                except:
                    # user tried to enter something other than 1-5, 'n', or 'quit'
                    print('That is not a valid rating, please enter a value 1-5:')
    
    # returns dataframe if they made changes to it, otherwise closes with no changes
    if to_return:
#         new_user_df = main_df
        return temp_df


# In[ ]:


def check_for_recs(user_id, username, password, main_df= None, movies_df=None):
    if len(main_df[main_df['userId'] == user_id]) < 5:
        temp_df = movie_recs(user_id, username, password, main_df, movies_df)
    else:
        make_more_recs = input('Would you like to rate more movies? (yes/no): ')
        if make_more_recs == 'yes':
            temp_df = movie_recs(user_id, username, password, main_df, movies_df)
        elif make_more_recs == 'no':
            pass
        else:
            print('You did not make a valid selection.')
           
       
    return temp_df


# In[ ]:


def start_program(new_user_df=None, movies_df=None, model=None):
    user_id, username, password = new_user(new_user_df)
    
    if user_id is not np.NaN:    
        temp_df = check_for_recs(user_id, username, password, new_user_df, movies_df)
        
        temp_df= make_rec(user_id, username, password, main_df=temp_df, model=model, movies_df=movies_df)
        
        
        return temp_df
    else:
        print('Program was terminated.')


# In[ ]:


def make_rec(user_id, username, password, main_df=None, model=None, movies_df=None):
    # list of all available genres
    genre_list = ['romance','fantasy','mystery','children','war','comedy',
                  'documentary','film-noir','thriller','action','sci-fi',
                  'drama','horror','crime','imax','animation','adventure',
                  'musical','western']
    # creating a while loop to keep the function opn
    keep_open = True
    print("(Enter 'quit' at any time to end the program.)")
    while keep_open == True:
        # seeing if user wants to review their recs
        rec = input('Would you like to retrieve your recommendations? (yes/no): ')
        if rec == 'yes':
            # Does the user want to limit results by genre?
            genre = input('Would you like recommendations from a specific genre? (yes/no): ')
            print('Compiling your recommendations...')
            # letting the user stop the program if they want to quit
            if genre == 'quit':
                print('Thank you for using the recommendation system.')
                print('Closing the program...')
                keep_open = False
                break      
            # If the user wants to limit results by genre
            elif genre == 'yes':
                print('Please select from the following list:')
                print('\t- romance','\n\t- fantasy','\n\t- mystery',
                      '\n\t- children','\n\t- war','\n\t- comedy',
                      '\n\t- documentary','\n\t- film-noir','\n\t- thriller',
                      '\n\t- action','\n\t- sci-fi','\n\t- drama','\n\t- horror',
                      '\n\t- crime','\n\t- imax','\n\t- animation','\n\t- adventure',
                      '\n\t- musical','\n\t- western')
                # Letting the user input specific genre
                genre_choice = input('Selection: ')
                # letting the user quit if they want to stop the program
                if genre_choice == 'quit':
                    print('Thank you for using the recommendation system.')
                    print('Closing the program...')
                    keep_open = False
                    break
                # Running the model with specified genre    
                elif genre_choice in genre_list:
                    print('Searching through specified genre...')
                    number_of_predictions = input('How many recommendations would you like? (1-50): ')
                    if number_of_predictions == 'quit':
                        print('Thank you for using the recommendation system.')
                        print('Closing the program...')
                        keep_open = False
                        break
                    else:
                        try:
                            number_of_predictions = int(number_of_predictions)
                            if number_of_predictions in list(range(1, 51)):
                                print('Processing request...')
                                rec_df = final_rec(user_id, number_of_predictions=number_of_predictions, model=model, main_df=main_df, movies_df=movies_df, genre=genre_choice)
                            else:
                                print('You did not select a valid response.')
                        except:
                            print('error: You did not select a valid response.')
                #telling the user that they didnt input valid response    
                else:
                    print('You did not select a valid response.')
            # running model with all genres
            elif genre == 'no':
                number_of_predictions = input('How many recommendations would you like? (1-50): ')
                if number_of_predictions == 'quit':
                    print('Thank you for using the recommendation system.')
                    print('Closing the program...')
                    keep_open = False
                    break
                else:
                    try:
                        number_of_predictions = int(number_of_predictions)
                        if number_of_predictions in list(range(1, 51)):
                            print('Processing request...')
                            rec_df = final_rec(user_id, number_of_predictions=number_of_predictions, model=model, main_df=main_df, movies_df=movies_df)
                        else:
                            print('You did not select a valid response.')
                    except:
                        print('error: You did not select a valid response.')
            else:
                # user did not enter a valid response
                print('You did not select a valid response.')
            
            
        # user does not want to receive recommendation now    
        elif rec == 'no':
            close_rec = input('Would you like to close the program? (yes/no): ')
            # closing recommendation
            if close_rec =='yes':
                print('Thank you for using the recommendation system.')
                print('Closing the program...')
                keep_open = False
                break
            # resetting so the user can get a rec if they want
            elif close_rec == 'no':
                continue
            #user did not input valid response
            else:
                print('You did not select a valid response.')
        # letting user quit program
        elif rec == 'quit':
            print('Thank you for using the recommendation system.')
            print('Closing the program...')
            keep_open = False
            break
        # user did not submit valid response
        else:
            print('You did not select a valid response.')
    
    return main_df


# In[ ]:


def final_rec(user_id, genre = None, number_of_predictions= 10, main_df = None, movies_df = None, model = None):
    # creating a dataframe with a specified user
    genre_list = ['romance','fantasy','mystery','children','war','comedy',
                  'documentary','film-noir','thriller','action','sci-fi',
                  'drama','horror','crime','imax','animation','adventure',
                  'musical','western']
    if genre == None:
        user_ratings = main_df[main_df['userId'] == user_id][['userId', 'movieId', 'rating']]
        # creating a dataframe with movies not yet reviewed
        user_predict = list(movies_df[~movies_df['movieId'].isin(user_ratings['movieId'].values)].movieId.values)
        # creating predictions and storing them in list
        predictions = []
        for movie in user_predict:
            predictions.append((movies_df['title'].loc[movies_df['movieId'] == movie].values[0],                                 model.predict(user_id, movie)[3]))
        
        predicted_df = pd.DataFrame(predictions, columns=['title', 'predicted rating']).sort_values('predicted rating', ascending=False).head(number_of_predictions)
        print(predicted_df)
    
    elif genre in genre_list:
        user_ratings = main_df[main_df['userId'] == user_id][['userId', 'movieId', 'rating']]
        # creating a dataframe with movies not yet reviewed
        user_predict = list(movies_df[~movies_df['movieId'].isin(user_ratings['movieId'].values)].movieId.values)
        # creating predictions and storing them in list
        predictions = []
        for movie in user_predict:
            predictions.append((movies_df['title'].loc[movies_df['movieId'] == movie].values[0],                                 model.predict(user_id, movie)[3]))
        
        predicted_df = pd.DataFrame(predictions, columns=['title', 'predicted rating']).sort_values('predicted rating', ascending=False)
        final_prediction = predicted_df.merge(movies_df).drop('movieId', axis=1)
        predicted_df = final_prediction[final_prediction['genres'].str.contains(genre)].drop(['genres', 'split_genres'], axis=1).head(number_of_predictions)
        print(predicted_df)
    else:
        print('You did not select a valid response.')
      
#     new_user_df = main_df
#     return main_df


def to_1D(series):
 return pd.Series([x for _list in series for x in _list])
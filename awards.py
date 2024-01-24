from awards_data import SAG, oscars, NBR, ISA, GLAAD, NAACP

# awards.py
# ENDG 233 F21
# Ibrahim Khalid
# UCID: 30207506
# A terminal-based program for analyzing movie awards data.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support strings, lists, dictionaries, sets, and tuples.
# Remember to include docstrings for your functions and comments throughout your code.
#


# ******************************************************************************************************
# Data is imported from the included awards_data.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
award_list_names = ['sag', 'oscars', 'nbr', 'isa', 'glaad', 'naacp']
award_list_options = [SAG, oscars, NBR, ISA, GLAAD, NAACP]
 
# ******************************************************************************************************



# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def count_awards(movie_title):
    '''
    output should return the amount of times the inputted movie won an award
    Parameters:
    movie_title (str): this is the input from the main line of code, which is the user's inputted movie that they want to check for its awards
    Returns:
    award_won (int): number of awards the movie has won
    '''
    award_won = 0    
    #define variable
    for movie in award_list_options: 
        #for loop: each element in the outer list                    
        for title in movie:                                 
            #for loop: each individual movie in the inner list
            if movie_title.upper() == title.upper():        
                #checks if input exists in inner list 
                award_won += 1                              
                #everytime the input movie is seen: value goes up by one, counting each time it shows up in the list
    return award_won                
#save value for later usage
    


def print_award_winners(awards):
    '''
    expected output should be the movies that were awarded by an organization(award_list_names)
    Parameters:
    awards (str): this is the input from the main line of code, which is the user's inputted movie organization
    Returns:
    entries (str): each individual movie within selected list
    '''
    counted_movie = 0 
    for movie in award_list_names:  #for each entry in the strings of the award organizations
        counted_movie += 1
        if awards == movie:            #if input = one of the strings of the award organization
            print('--Requested Award Winners--')
            for entries in award_list_options[counted_movie-1]:         #selects from which list to print the movies from 
                print(entries)



# ******************************************************************************************************

print("ENDG 233 Awards Data Program")

# DEFINE MAIN CODE BELOW
user_input = int(input("\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "))
while user_input != 0:              
    #code for when the input is for a specific function and does not end the program
    if user_input == 1:             
        #first input: calls the function that will count how many awards the inputted movie won
        movie_title = input("Please enter the movie title you would like to search: ").strip().upper() 
        #removes whitespace and makes it uppercase
        print(f'--Number of Awards Won--\n {count_awards(movie_title)}') 
        #calls function that will output number of awards won by the movie
    elif user_input == 2:
        awards = input("\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n").strip().lower() 
        #removes whitespace: makes it LOWERCASE because the dataset involving the names of the organizations is lowercase
        if awards not in award_list_names: 
            #if inputted movie is not in the list of organizations
            print('Awards list not found')
            print_award_winners('Awards list not found.')
        else:
            print_award_winners(awards)
            #output: print movies that were given awards by the specified organization 
    else:
        print("You must select either 1, 2, or 0.")
        #when other integers are entered: e.g 3,4,5,6, print error message adn try again
    user_input = int(input("\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "))
else: 
    print('Thank you for using the awards data program.')
#this is when the user enters 0, this exits the while loop. and then closes the program
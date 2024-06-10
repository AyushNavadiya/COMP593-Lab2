
# TODO: STEP 1 - START WRITING THE SCRIPT

def main():
    # TODO: STEP 2 - CREATE A COMPLEX DATA STRUCTURE
    data_structure = {
        "full_name": "Ayush Navadiya",
        "student_id": 10321544,
        "pizza_toppings": ["Pineapple", "cheese", "Olives"],
        "movies": [
            {
                "title": "kung fu panda",
                "genre": "action"
            },
            {
                "title": "Minions",
                "genre": "cartoon"
            }
        ]
    }

    # TODO: STEP 3 - ADD ANOTHER MOVIE TO THE DATA STRUCTURE
    new_movie = {
        "title": "Tom and Jerry",
        "genre": "animation"
    }
    data_structure["movies"].append(new_movie)

    #STEP 4 - function call to print stuent name and ID
    print_student(data_structure)

    #STEP 6 - function call before Adding
    print_pizza_toppings(data_structure)

    #STEP 5 - Function call to add pizza topings
    more_pizza_topings = ('tomato', 'onion')
    add_pizza_toppings(data_structure, more_pizza_topings)

    #STEP 6 - function call after Adding
    print_pizza_toppings(data_structure)

    #STEP 7 - function call to print movie genere
    print_movies_genere(data_structure)

    #STEP 8 - function call to print movie title
    print_movies_title(data_structure['movies'])

    
# TODO : STEP 4 - USE A FUNCTION TO PRINT STUDENT NAME AND ID
def print_student(data_structure):
    firstname = data_structure["full_name"].split(); 
    print(f"My name is {data_structure['full_name']}, but you can call me Mr {firstname[0]} ")
    print(f"My student ID is {data_structure["student_id"]}. \n")

# TODO STEP 5 - USE A FUNCTION TO ADD PIZZA TOPPINGS TO THE DATA STRUCTURE
def add_pizza_toppings(data_structure, pizza_toppings):
    #add toppings to the list
    data_structure['pizza_toppings'] += pizza_toppings
    #sorting the list
    data_structure['pizza_toppings'] = sorted(data_structure['pizza_toppings'], key=str.casefold)
    #lower case conversion
    data_structure['pizza_toppings'] = [string.lower() for string in data_structure['pizza_toppings']]

# TODO STEP 6 - USE A FUNCTION TO PRINT A BULLET LIST OF PIZZA TOPPINGS
def print_pizza_toppings(data_structure):
    #print pizza toppings bulleted list
    print(f"My favorite pizza toppings are:")
    for toppings in data_structure['pizza_toppings']:
        print(f"- {toppings}") 
    print("")

# TODO STEP 7 - USE A FUNCTION TO PRINT A COMMA-SEPARATED LIST OF MOVIE GENRES
def print_movies_genere(data_structure):
    length = len(data_structure['movies'])
    i = 0
    print('I like to watch', end=" ")
    #print movie genere
    for movies in data_structure['movies']:
        #while loop to add and before the last movie
        while i < length: 
            i = i + 1
            if(i == length):
                print(f'and {movies['genre']} movies', end='.')
                break
            else:
                print(f'{movies['genre']}', end=', ')
                break
    print("\n")


# TODO STEP 8 - USE A FUNCTION TO PRINT A COMMA-SEPARATED LIST OF MOVIE TITLES
def print_movies_title(movies_list):
    length = len(movies_list)
    i = 0
    print('Some of my favourite movies are', end=" ")
    #print movies title
    for movies in movies_list:
        #while loop to add and before the last movie
        while i < length: 
            i = i + 1
            if(i == length):
                print(f'and {movies['title']}', end='!')
                break
            else:
                print(f'{movies['title']}', end=', ')
                break


if __name__ == '__main__':
    main()
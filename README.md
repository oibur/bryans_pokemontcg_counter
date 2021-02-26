# python-project-2021
Bryan McGill

My project displays how many times each Pokemon has been featured on a card, over the 94 standard TCG sets.
-Using JSON files I found at https://github.com/PokemonTCG/pokemon-tcg-data (Feature#5) I cut the data I needed using a loop function (Feature#6(1/3)) in dexlist_from_json.py. 
-Then I compile the data lists from each JSON file into one data list (Feature#3) using another loop function (Feature#6(2/3)) in compile_dexlists.py. 
-Finally I call a loop function (Feature#6(3/3)) in manipulate_data.py to create a .txt file that displays (Feature#12) how many times each Pokemon has been featured on a card. 
-To produce this txt file simply run manipulate_dexlists.py in the using_json folder.

***Features still to add!***
13) Visualize data in a graph, chart, or other visual representation of data

16) Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display

***February 25th, 2021 - Using the API***
I have completed steps1-3 using json files downloaded from the API, however I have run into some roadblocks including 1) havinig to pass on a UnicodeError I don't understand in 'compile_dexlists.py' 2) not every Pokemon being returned, or being returned with incomplete data. I am hoping that working with the API can give me more direct results by retreiving it with 1 function vs. 3 currently, and then I can focus more on vizualizing (the correct) data!

***February 15th, 2021 - Update***
Step 1 - Complete through JSON files.
Step 2 - I have figured out how to isolate the needed data from the JSON files.
        *Need to figure out how to loop through files, pull the data I need and append it to single dict.
        *Need to figure out any hiccups I may encounter with some Pokemon having varied names (EX, GX, V)
Step 3 - Hoping this step will be fairly straight-forward.
Step 4 - Doing well, and feel ahead of schedule, so this step should be achievable.

***January 30th, 2021 - Creating a Plan***
My goal is to use python to count how many times each pokemon appears in the TCG and display this information as a list/chart, as well as a graph. I aim to order the appearances from most times (likely Pikachu) to least times (likely Mantyke), as well as ordered by Pokedex #. This information is interesting to me because it might have a correlation to which Pokemon are the most popular, and potentially have more collectibility value. 

Step 1 - Access the data available online.
    - This will either be downloaded in JSON form from https://github.com/PokemonTCG/pokemon-tcg-data/tree/master/json/cards or hopefully I will be able to access and import it from this API https://pokemontcg.io/

Step 2 - Organize/Cut the data down to what I need
    - There is A LOT of uneeded data that is also supplied. a) Can I find better/more appropriate data elsewhere? b) How can I cut/organize it in a way that will make sense to this project. I think I'd rather use this data than search elsewhere because I can see myself using it for other things in the future and it would be good to learn my way around it.

Step 3 - Sort the data 
    - I'm assuming the sort method will do what I need to sort the Pokemon from most appearances to least appearances, but I'm sure there will be some hiccups. One problem I can think of I may run into is some cards have the name "Erika's Bulbasaur" instead of just "Bulbasaur". Could this affect my results?

Step 4 - Visualize the data in graphs!
    - My most-to-least is OK to be displayed in a list and make sense. But I want to visualize the data in a graph ordered by Pokedex # as well. This is going to be the most challenging part of this project. As I believe I will have to use libraries to visualize the data and I have not used any yet. Also there are nearly 900 pokemon, so I will have to figure out a way to break the graph down in a way that still makes sense (i.e. generation)
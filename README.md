# python-project-2021
Bryan McGill

Project includes a README file that explains the following:
    a) A one paragraph or longer description of what your project is
    b) Which 3+ features you have included from the below lists to meet the requirements
    c) Any special instructions required for the reviewer to run your project
    *) Features List Below

***February 15, 2021 - Update***
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
    

***Features List:***

2) Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code

3) Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program

5) Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

6) Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code. For example, you could create a function that reads how many items there are in a text file, returns that value, and later uses that value to execute a loop a certain number of times.

8) Connect to an external/3rd party API and read data into your app

10) Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams)

12) Analyze text and display information about it (ex: how many words in a paragraph)

13) Visualize data in a graph, chart, or other visual representation of data

14) Implement a “scraper” that can be fed a type of file or URL and pull information off of it. For example, a web scraper that lets you provide any website URL and it will find certain keywords on the page

15) Implement optical character recognition (OCR) that you can upload PDFs to and it will generate the text 

16) Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display
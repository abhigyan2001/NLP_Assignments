# Assignment 1 - Basic Text Processing on Cranfield Dataset

To run your code, run main.py with the appropriate arguments as shown below:

Usage: 
````
main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
        [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 
````

When the -custom flag is passed, the system will take a query from the user as input. When the flag is not passed, all the queries in the Cranfield dataset are considered, for example:

````
> python main.py -custom
> Enter query below
> Papers on Aerodynamics
````

This will generate *queries.txt files in the OUTPUT FOLDER after each stage of preprocessing of the query and *docs.txt files in the OUTPUT FOLDER after each stage of preprocessing of the documents.
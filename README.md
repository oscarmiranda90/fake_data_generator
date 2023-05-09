# fake_data_generator
a fake data generator, creates 2 csvs, one contains Users with: user_id, first name, last name, country,
city, email and the other csv contains buy orders with user_id, item
, date, order_id, i created this to practice my SQL queries.


made by Oscar Crescente
for practice purposes on Sql



a fake data generator, creates 2 csvs, one contains Users with: user_id, first name, last name, country, city, 
email and the other csv contains buy orders with user_id, item, date, order_id, i created this to practice my SQL queries or any 
other necessity you may have.



- data_list.py -

contains the lists of random names, items, cities and countries (USA, CANADA AND MEXICO)
so they are used by data_generator in the functions

- data_generator.py -

contains the functions to use the program and generates 2 csvs with the data you need




#### IMPORTANT ####

i set as a limit for rows 10.000 data rows, just in case, but you can change it easily on
the code

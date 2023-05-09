### This is a simple fake data creator i made to practice queries on SQL, you can use it as you see fit :)
### Oscar Crescente oscar.crescente@icloud.com
import random
from datetime import datetime, timedelta
import data_lists
import csv

user_list = []
order_list = []

# creates orders (buys) according to the number of users created on generator()
def generator_order(number):
    count = 0
    while count <= number:
        # create every variable
        item = random.choice(data_lists.items)
        start_date = datetime(2021, 1, 1)  # Starting date
        end_date = datetime(2023, 12, 31)  # Ending date

        # Generate 10 random dates between start_date and end_date
        for i in range(number):
            date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
            random_date = date.strftime('%Y-%m-%d')

        # create a random number to work as user id
        random_user = str(random.randint(0, number)).zfill(5)

        # create a random number as order number
        order_id = str(random.randint(100000, 999999)).zfill(5)

        ## print the full data set
        order_list.append(['(' + f'{random_user}', f"'{order_id}'", f"'{item}'", f"'{random_date}')",''])
        count += 1
        with open('order_data.csv', mode='w', newline='', encoding='UTF8') as file:
            writer = csv.writer(file)
            for row in order_list:
                writer.writerow(row)
    print('''
            Thanks for using this Fake data creator
            please check your folder, you can see 
            there user_data.csv and order_data.csv
            use it as you see fit.
        ''')
# creates users
def generator(number):
    count = 0
    while  count <= number:
        # create every variable
        name = random.choice(data_lists.first_names)
        surname = random.choice(data_lists.last_names)
        emailchoice = random.choice(data_lists.email_suffix)
        mail = name.lower() +'_'+ surname.lower() + emailchoice
        nation = random.choice(list(data_lists.country_keys))
        city = random.choice(data_lists.countries_cities[nation])


        ## print the full data set
        formatted_count = '{:05d}'.format(count) # 00001 format for the id
        # for some weird reason if i added at the end a comma between " , " the final output gave me something that
        # does not work on SQL
        user_list.append(['(' + f'{formatted_count}', f"'{name}'", f"'{surname}'", f"'{nation}'", f"'{city}'", f"'{mail}')",''])
        count += 1


        with open('user_data.csv', mode='w', newline='', encoding='UTF8') as file:
            writer = csv.writer(file)
            for row in user_list:
                writer.writerow(row)
    # invoking the buy order creator
    generator_order(number)
# initializes the program, asks for the number of rows we want, and creates 2 Csvs user_data and order_data.
def crear_dataset():
    while True:
        try:
            entry = int(input('inserte la cantidad de rows que desea: '))
            # HERE IS THE ROW LIMIT if you want more row entries change this number
            if entry <= 10000:
                generator(entry)
                break
            else:
                print('please use a number lower than 10.000')
        except ValueError:
            print('You must input a number!')


crear_dataset()

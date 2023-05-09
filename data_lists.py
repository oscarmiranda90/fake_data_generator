# here we store data as names, suffixes, countries, etc.
import random

first_names = ['Danielle','Delilah','Imogene','Jade','Anne','Aquila','Alexander','Yen','Michael','Amy','Warren','Maisie',\
        'Josephine','Aidan','Phelan','Flavia','Yuri','Chava','Abdul','Gail','Carlos','Thaddeus','Emery','Vance','Kermit',\
        'Karina','Colby','Florence','Adrienne','Anne','Blaze','Dominique','Mariam','Anika','Benjamin','Jessica','Athena',\
        'Dara','Valentine','Signe','Kylan','Shoshana','Camden','Merrill','Vera','Elvis','Whoopi','Tatyana','Barbara',\
        'Zia','Mia','Yen','Colton','Samson','Kibo','Charlotte','Risa','Addison','Hamilton','Cheyenne','Aquila','Garth',\
        'Ivan','Jonas','Rylee','Zena','Marsden','Adara','Vielka','Elijah','Jared','Cruz','Vincent','Orlando','Irene',\
        'Russell','Amal','Bo','Quail','Lane','Vladimir','Shellie','Knox','Kelly','Galvin','Maryam','Cooper','Martin',\
        'Elijah','Phelan','Amethyst','Hector','Gay','Nigel','Amir','Donovan','Maryam','Elmo','Breanna','India',\
        'Anastasia','Ivory','Diana','Ira','Scarlett','Coby','Kameko','Rhiannon','Irene','Lee','Odette','Erasmus',\
        'Phoebe','Hu','Nero','Steven','Kenneth','Ora','Steel','Eugenia','Ethan','Cooper','Bryar','Mechelle','Rigel',\
        'Maxwell','Alden','Malcolm','Geoffrey','Mallory','Branden','Adara','Quynn','Idona','Zelda','Amethyst','Morgan',\
        'Peter','Carly','Drake','Ferris','Murphy','Kevyn','Abigail','Xanthus','Xandra','Brock','Porter','Elaine',\
        'Tatyana','Lee','Alea','Brock','Perry','Hiroko','Peter','Carter','Sandra','Zachery','Hilda','Lacy','Urielle',\
        'Ava','Shafira','Kelsie','Melvin','Lester','Denton','Elijah','Jonas','Felicia','Ashton','Chadwick','Amos',\
        'Cade','Genevieve','Riley','Basil','Yvonne','Ignatius','Audra','Castor','Kerry','Mercedes','Abel','Cullen',\
        'Darrel','Benjamin','Tanya','Xandra','Noble','Selma','Phyllis','Cecilia','Sara','Brendan','MacKensie','Jane',\
        'Brent','Talon','Lillian','Geraldine','Dustin','Yoshi','Armand','Kevyn','Edan','Barclay','Cassandra','Stacy',\
        'Driscoll','Abraham','Henry','Tara','Jason','Delilah','Gary','Tobias','Macaulay','Maryam','Jessamine','Baker',\
        'Jessamine','Whilemina','Brendan','Nomlanga','Burton','Imelda','Frances','Karly','Peter','Amity','Nigel','Reed',\
        'Rudyard','Chanda','Jacqueline','Lilah','Rafael','Rama','Britanney','Tana','Mara','Aileen','Shafira','Savannah',\
        'Cody','Hayley','Kylie','Kathleen','Stacey','Buckminster','Davis','Liberty','Zenaida','Xaviera','Drew','Bell',\
        'Quentin','Ivory','Rudyard','Kenyon','Lenore','Selma','Michelle','Amela','Whoopi','Adrienne','Maisie','Igor',\
        'Finn','Tate','Allistair','Lael','Sonya','Kiona','Hop','Samuel','Kylie','Ralph','Alfreda','Leandra','Lacey',\
        'Hadley','Simon','Germane','Hedley','Jescie','Kellie','Lois','Ronan','Giacomo','Buffy','Emery','Xaviera',\
        'Hermione','Wing','Ivana','Autumn','Charles','Hector','Nora','Jonas','Ethan','Montana','Flynn','Idona','Tasha',\
        'Mallory','Jarrod','Gemma','Cooper','Stone','Dai','Chester','Hollee','Buckminster','Yoshio','Arthur',\
        'Genevieve','Alfonso','Debra','Solomon','Akeem','Ashton','Jemima','Dean','Hadassah','Clinton','Kay','Hedley',\
        'Chloe','Flavia','Timothy','Whilemina','Nicole','Devin','Nell','Hedy','Nash','Ori','Cooper','Sawyer','Salvador',\
        'Amethyst','Leandra','Rhonda','Jerry','Alika','Serena','Marvin','Benjamin','Carissa','Ora','Tate','Colette',\
        'Martin','Zelenia','Bethany','Calvin','Julian','Quin','Hanae','Allegra','Doris','Carly','Lucius','Darryl',\
        'Hanae','Florence','Bruce','Curran','Gary','Violet','Finn','Blake','Nita','Leonard','Merritt','Liberty','Ruby',\
        'Ronan','Echo','Salvador','Reece','Camille','Jonah','Dominic','Cade','Axel','Lacota','Maile','Leila','Carl',\
        'Lara','Cheyenne','Thane','Matthew','Francis','Jemima','Regina','Juliet','Summer','Ignacia','Ariana','Edward',\
        'TaShya','Keegan','Georgia','Heather','Doris','Kylee','Shaine','Dominique','Brent','Kadeem','Wynne','Chaim',\
        'Fulton','Kerry','Heather','Cameron','Kirestin','Yen','Justina','Mariko','Tasha','Delilah','Sopoline','Ingrid',\
        'Stuart','Theodore','Acton','Anthony','Marshall','Jacob','Pascale','Andrew','Mona','Ross','Amaya','Kathleen',\
        'Tanisha','Randall','Howard','Kiayada','Hayes','Ivana','Adrienne','Arsenio','Cruz','Deanna','Deirdre','Quemby',\
        'Zena','Quinlan','Blake','Ira','Ruth','Declan','Duncan','Perry','Sierra','Bryar','Yasir','Laura','Otto','Tanek',\
        'Jasper','Cheryl','Nina','Lee','Maisie','Laith','Erich','Yoshio','Brennan','Ivory','Peter','Kane','Kelly',\
        'Kelly','Baxter','Quail','Chancellor','Chiquita','Adena','Evan','Vielka','Bree','Len','Katell','Evan','Miriam',\
        'Kenneth','Audrey','Maggy','Farrah','Kieran','Minerva']

last_names = ['last_name','Ortega','Merritt','Owens','Walter','Hurst','Gregory','Johnson','Rollins','Baldwin',
              'Hawkins','Frank','Graham','Page','Sykes','Fisher','Carey','Carver','Hill','Hanson','Burgess','Ramsey',
              'Robles','Jackson','Davidson','Ewing','Clay','Christensen','Stewart','Duncan','Welch','Delacruz',
              'Lambert','Mckinney','Nelson','Garrison','Gardner','Coleman','Mccormick','Lloyd','Miranda','Curry',
              'Emerson','Saunders','Gibbs','Burnett','Ratliff','Mclaughlin','Tanner','Mccray','Knox','Hobbs','Valdez',
              'James','Love','Rutledge','Compton','Nash','Ratliff','Wilson','David','Roberts','Sykes','Cleveland',
              'Rosa','Finley','Strickland','Gilliam','Hodges','Justice','Jefferson','Barry','Thornton','Avery',
              'Salazar','Horn','Moon','Griffin','Mcleod','Richmond','Wood','Neal','Cherry','Edwards','Lee','Duncan',
              'Valdez','Taylor','Page','Byrd','Hicks','Chambers','Acosta','Holland','Jennings','Kemp','Bauer',
              'Buchanan','Gibbs','Norton','Mckinney','Hodge','Espinoza','Ware','Buck','Richard','Banks','Hansen',
              'Jacobson','Snow','Hodge','Henderson','Cain','Mccormick','Callahan','Carey','Downs','Wiggins',
              'Hoffman','Hooper','Terry','Wilkins','Melton','Rosa','Hall','Berger','Rivera','Langley','Knox',
              'Guerrero','Espinoza','Rogers','Fitzpatrick','Meadows','Doyle','Sellers','Dickson','Rasmussen',
              'Haley','Mcconnell','Ayala','Gray','Haney','Myers','Calhoun','Cannon','Sharp','Snider','Huber',
              'Luna','Lowery','Bridges','Acosta','Welch','Burgess','Frye','Fuentes','Case','Wilcox','Ferrell',
              'Molina','Hanson','Houston','Huber','Adkins','Weaver','Mcconnell','Garrett','Curry','Crane','Weaver',
              'Wilkins','Lloyd','Nolan','Stone','Wells','Griffith','Jenkins','Vincent','Roth','Gill','Johnson',
              'Barry','James','George','Ford','Duffy','Foley','Castro','Flynn','Coffey','Merritt','Wiley','Murphy',
              'Robbins','Ferguson','Hudson','Kinney','Heath','Wiley','Payne','Hensley','Pittman','Wynn','Crawford',
              'Berry','Gardner','Ashley','Holden','Bryan','Frazier','Shannon','Hubbard','Rhodes','Ferguson','Neal',
              'Hickman','Holden','Bernard','Macias','Fox','Kaufman','Justice','Stephens','Shaffer','Brennan','Oliver',
              'Woodward','Hendricks','Griffith','Sutton','Hunter','Hill','Sanders','Finley','Trevino','Gross','Combs',
              'Molina','Oneil','Fleming','Guzman','Myers','Baldwin','Pearson','Burt','Noble','Michael','Spears',
              'Greene','Mccray','Foster','Carver','Townsend','Abbott','Frank','Rojas','Livingston','Maldonado',
              'Byers','Mcmillan','Sharpe','Navarro','Walter','Hammond','Pennington','Johns','Giles','Jacobson',
              'Dominguez','Horne','Montoya','Sanford','Morris','Nash','Freeman','Mclaughlin','Ochoa','Flynn',
              'Murphy','Figueroa','Reyes','Forbes','Sheppard','Kelley','Kirk','Pena','Lyons','Herrera','Phelps',
              'Lamb','Rhodes','Lynn','Ferguson','Beasley','Caldwell','Lynn','Gilbert','Russo','Wall','Grant',
              'Mann','Bates','Blake','Parsons','Kelly','Barnett','Cooley','Ortega','Reyes','Briggs','Henson',
              'Joseph','Hanson','Phillips','Padilla','Hebert','Jennings','Pace','Cummings','Buck','Moran',
              'Morin','Mcgee','Newton','Riddle','Ward','Rocha','Barnett','Knox','Rivas','Sweet','Kirby','Duran',
              'Logan','Avila','Fuller','Shepard','Harmon','Terrell','Cooper','Mcclain','Daniels','Beach','Stevens',
              'Dejesus','Bryan','Berger','Crawford','Albert','Shaffer','Chase','Morton','Chen','Sosa','Mendez','Woods',
              'Rhodes','Madden','Branch','Gentry','Ramsey','Harding','Walls','Poole','Ramos','Copeland','Lynn',
              'Aguilar','Bradford','Rosales','Bruce','Rush','Vang','Britt','Roberson','Morin','Soto','Johnson',
              'Knapp','Kane','Solomon','Ford','Sargent','Macias','Moran','Hanson','Burks','Blevins','Dennis',
              'Russell','Page','Campbell','Guy','Chambers','Beach','Mcdonald','Rivera','Doyle','Briggs','Weiss',
              'Duran','George','Odom','Ruiz','Stein','Farley','Fowler','Page','Bates','Huff','Sweeney','Mccarthy',
              'Rush','Clemons','Romero','Osborn','Short','Mendez','Merritt','Singleton','Hughes','Franco','Becker',
              'Santos','Kane','Hall','Hoffman','Hood','Pate','Hess','Vega','Mcmillan','Foreman','Sutton','Hobbs',
              'Roman','Ball','Briggs','Charles','Whitney','Snyder','Vaughn','Todd','Mayo','Marshall','Beck','Rocha',
              'Vinson','Patton','Whitaker','Spencer','Santana','Gibson','Gomez','Velasquez','Hopper','Mccullough',
              'Miles','Robles','Holmes','Hansen','Velasquez','Jordan','Hill','Donaldson','Mcconnell','Hobbs','Woodard',
              'Mays','Ratliff','Wong','Russo','Payne','House','Emerson','Donaldson','Evans','Reynolds','Holland',
              'Fletcher','Browning','Williamson','Calhoun','Frye','Acosta','Reynolds','Contreras','Benson','Mullen',
              'Hodge','Chan','Gutierrez','Hancock','Lott','Turner','Newton','Coleman','Watson','Hutchinson','Hopper']

countries_cities = {
    'USA': ["Casper", "Southaven", "Columbus", "Atlanta", "Memphis", "Colorado Springs", "Aurora", "Idaho Falls",
            "Reno",
            "Springfield", "Phoenix", "Allentown", "Columbus", "Sacramento", "Henderson", "Iowa City", "Fort Worth",
            "Cheyenne", "Little Rock", "Rochester", "Fairbanks", "San Diego", "Baltimore", "Springdale", "Columbus",
            "Philadelphia", "Sandy", "Minneapolis", "Gaithersburg", "Kenosha", "Tampa", "Hilo", "Wichita", "Rockford",
            "Phoenix", "Tampa", "Miami", "Nashville", "Lansing", "Great Falls", "Gillette", "Boston", "Southaven",
            "South Portland", "Rutland", "Chattanooga", "Olathe", "Sandy", "Spokane", "Frankfort", "Hattiesburg",
            "Henderson", "Dallas", "San Jose", "Clarksville", "College", "Fort Collins", "Chattanooga", "Topeka",
            "Richmond", "Naperville", "Waterbury", "Rockville", "Owensboro", "Salem", "Lowell", "Rockville",
            "West Valley City", "Cedar Rapids", "Bridgeport", "Essex", "Gulfport", "Jackson", "Rockford", "Great Falls",
            "San Antonio", "Wilmington", "Spokane", "Burlington", "Bozeman", "Frankfort", "Portland", "Saint Paul",
            "Honolulu", "Philadelphia", "Green Bay", "Evansville", "Billings", "Toledo", "Columbia", "Iowa City",
            "Memphis", "Pittsburgh", "Fresno", "Cedar Rapids", "Rockford", "Idaho Falls", "Birmingham", "Birmingham",
            "Frankfort"],
    'Canada': ["Tulita", "Tofield", "Stratford", "Gander", "Watson Lake", "Brandon", "Lamont", "Dieppe", "Vaughan",
               "Abbotsford", "Gander", "Wekweti", "Merritt", "Whitchurch-Stouffville", "Dubuisson", "Gjoa Haven",
               "Williams Lake", "Pitt Meadows", "Stratford", "Iqaluit", "Canora", "Lacombe", "Yorkton", "Kitchener",
               "Marystown", "Outremont", "Annapolis County", "Flin Flon", "Whitehorse", "Rae Lakes", "Bon Accord",
               "Iqaluit", "Richmond", "Stonewall", "Lions Bay", "Cumberland County", "Arviat", "Moncton", "Hamilton",
               "Westlock", "Beausejour", "Richmond", "Whitehorse", "Watson Lake", "Montague", "Calder", "Stonewall",
               "Whitehorse", "Saint John", "Moose Jaw", "Watson Lake", "Charlottetown", "Port Moody", "Burlington",
               "Cornwall", "Nakusp", "LaSalle", "Watson Lake", "Tay", "Baddeck", "Maple Creek", "Lourdes",
               "Watson Lake",
               "Gibsons", "Macklin", "Carbonear", "Flin Flon", "Innisfail", "Moose Jaw", "Inuvik", "Regina",
               "Drayton Valley", "Williams Lake", "Gjoa Haven", "Montague", "Lang", "Bay Roberts", "Watson Lake",
               "Guysborough", "Ville de Maniwaki", "Glovertown", "Wolfville", "Carbonear", "Gatineau", "Lanark County",
               "Montague", "Campbellton", "Langenburg", "Whitehorse", "Whitehorse", "Bathurst", "Fort Saskatchewan",
               "Fredericton", "White Rock", "Owen Sound", "Minitonas", "Yorkton", "Municipal District", "Whitehorse",
               "Watson Lake"],
    'Mexico': ["Los Mochis", "Acuña", "Veracruz", "Tonalá", "Villahermosa", "Tehuacán", "Saltillo", "Veracruz",
               "Uruapan",
               "Zamora de Hidalgo", "Mexico City", "Chilpancingo", "Tuxtla Gutiérrez", "San Juan del Río", "Mérida",
               "Torreón", "Villahermosa", "Soledad de Graciano Sánchez", "Salamanca", "Pachuca", "Minatitlán",
               "Chihuahua",
               "San Pedro Garza García", "Reynosa", "San Nicolás de los Garza", "Matamoros", "Morelia",
               "Soledad de Graciano Sánchez", "Iguala", "Ensenada", "Hermosillo", "Ensenada", "Mérida", "Tlaquepaque",
               "Mérida", "Cuernavaca", "Oaxaca", "Tapachula", "Irapuato", "Mazatlán", "Oaxaca", "Chihuahua",
               "Zamora de Hidalgo", "Pachuca", "Chilpancingo", "Mexico City", "León", "Villahermosa",
               "Ciudad Santa Catarina", "Tijuana", "Mérida", "Minatitlán", "Hermosillo", "Mexicali",
               "Hidalgo del Parral",
               "San Cristóbal de las Casas", "Mérida", "Jiutepec", "San Luis Río Colorado", "Ciudad Madero",
               "Cuernavaca",
               "Salamanca", "Mexico City", "Mexico City", "Uruapan", "Saltillo", "San Juan del Río", "Guadalupe",
               "Morelia", "Pachuca", "Villahermosa", "Tampico", "Tehuacán", "Celaya", "Mérida", "Zapopan", "Pachuca",
               "Mérida", "Juárez", "Ciudad Valles", "Mérida", "Jiutepec", "Mexico City", "Tapachula", "Villahermosa",
               "Cuernavaca", "San Juan del Río", "General Escobedo", "Oaxaca", "Pachuca", "Iguala",
               "Hidalgo del Parral",
               "San Juan del Río", "Oaxaca", "León", "Mérida", "Mazatlán", "Jiutepec", "San Juan del Río",
               "Ciudad Santa Catarina"]}

email_suffix = ['@hotmail.com', '@yahoo.com', '@gmail.com', '@icloud.com', '@protonmail.com']

items = ['Milk', 'Bread', 'Eggs', 'Butter', 'Cheese', 'Yogurt', 'Ice Cream', 'Orange Juice', 'Apple Juice',
                 'Bananas', 'Apples', 'Oranges', 'Grapes', 'Strawberries', 'Blueberries', 'Raspberries', 'Blackberries',
                 'Watermelon', 'Cantaloupe', 'Honeydew', 'Pineapple', 'Mango', 'Peaches', 'Plums', 'Pears', 'Grapefruit',
                 'Lemons', 'Limes', 'Carrots', 'Broccoli', 'Cauliflower', 'Cucumbers', 'Tomatoes', 'Potatoes', 'Onions',
                 'Garlic', 'Mushrooms', 'Green Beans', 'Corn', 'Peas', 'Lettuce', 'Spinach', 'Kale', 'Arugula', 'Cabbage',
                 'Bell Peppers', 'Chili Peppers', 'Jalapenos', 'Avocado', 'Olives', 'Pickles', 'Mayonnaise', 'Ketchup',
                 'Mustard', 'Hot Sauce', 'BBQ Sauce', 'Salsa', 'Pasta', 'Rice', 'Quinoa', 'Couscous', 'Breadcrumbs',
                 'Flour', 'Sugar', 'Salt', 'Pepper', 'Cinnamon', 'Vanilla Extract', 'Olive Oil', 'Vegetable Oil',
                 'Canola Oil', 'Coconut Oil', 'Peanut Butter', 'Jelly', 'Jam', 'Honey', 'Maple Syrup', 'Pancake Mix',
                 'Waffle Mix', 'Baking Powder', 'Baking Soda', 'Yeast', 'Cake Mix', 'Brownie Mix', 'Cookie Mix',
                 'Chocolate Chips', 'Nuts', 'Dried Fruit', 'Trail Mix', 'Granola Bars', 'Cereal', 'Oatmeal', 'Crackers',
                 'Chips', 'Pretzels', 'Popcorn', 'Noodles', 'Soup', 'Broth', 'Canned Vegetables', 'Canned Fruit',
                 'Canned Meat', 'Canned Fish', 'Tuna', 'Salmon', 'Chicken', 'Ground Beef', 'Steak', 'Pork Chops',
                 'Sausage', 'Bacon', 'Ham', 'Hot Dogs', 'Chicken Nuggets', 'Frozen Vegetables', 'Frozen Fruit',
                 'Frozen Pizza', 'Frozen Dinners', 'Frozen Meat', 'Frozen Fish', 'Frozen Chicken', 'Frozen Waffles',
                 'Ice', 'Bottled Water', 'Soda', 'Juice Boxes', 'Tea', 'Coffee', 'Energy Drinks', 'Alcohol', 'Wine',
                 'Beer', 'Chips and Salsa', 'Cheese and Crackers', 'Popcorn and Candy', 'Ice Cream Cones',
                 'Popsicles', 'Cookies', 'Brownies', 'Donuts', 'Cupcakes', 'Birthday Candles', 'Party Decorations']




# these are going to be used in data_generator.py to assign random countries and cities.

country_keys = countries_cities.keys()           # picking the keys from the dict
country_select = random.choice(list(country_keys))   # picking a random choice from the keys turned into list
city_pick = random.choice(countries_cities[country_select])  #  choosing a random value from each key to assign a city



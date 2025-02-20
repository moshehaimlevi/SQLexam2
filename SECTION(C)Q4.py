############################################################################################################# SECTION A:

import sqlite3

conn = sqlite3.connect('SQLite.exam.q4')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL UNIQUE,
    genre TEXT NOT NULL,
    country TEXT NOT NULL,
    language TEXT NOT NULL,
    year INTEGER NOT NULL CHECK (year >= 2009),
    revenue REAL NOT NULL CHECK (revenue >= 0)
);
''')

conn.commit()

insert_query = '''
INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
('Oppenheimer', 'Biography', 'USA', 'English', 2023, 960),
('Barbie', 'Comedy', 'USA', 'English', 2023, 1440),
('Dune Part Two', 'Sci-Fi', 'USA', 'English', 2024, 700),
('John Wick 4', 'Action', 'USA', 'English', 2023, 440),
('Everything Everywhere All at Once', 'Sci-Fi', 'USA', 'English', 2022, 140),
('The Batman', 'Action', 'USA', 'English', 2022, 772),
('Spider Man No Way Home', 'Action', 'USA', 'English', 2021, 1920),
('Top Gun Maverick', 'Action', 'USA', 'English', 2022, 1490),
('The Whale', 'Drama', 'USA', 'English', 2022, 55),
('Guardians of the Galaxy Vol 3', 'Action', 'USA', 'English', 2023, 845),
('Parasite', 'Thriller', 'South Korea', 'Korean', 2019, 266),
('Train to Busan 2', 'Horror', 'South Korea', 'Korean', 2020, 92),
('Decision to Leave', 'Mystery', 'South Korea', 'Korean', 2022, 23),
('Joker', 'Drama', 'USA', 'English', 2019, 1074),
('Tenet', 'Sci-Fi', 'USA', 'English', 2020, 365),
('The Irishman', 'Crime', 'USA', 'English', 2019, 8),
('Ford v Ferrari', 'Drama', 'USA', 'English', 2019, 225),
('1917', 'War', 'UK', 'English', 2019, 385),
('The Farewell', 'Drama', 'USA', 'English/Chinese', 2019, 23),
('The Banshees of Inisherin', 'Comedy', 'Ireland', 'English', 2022, 49),
('Django Unchained', 'Western', 'USA', 'English', 2012, 426),
('Avengers Endgame', 'Action', 'USA', 'English', 2019, 2798),
('Black Panther', 'Action', 'USA', 'English', 2018, 1347),
('Coco', 'Animation', 'USA', 'English/Spanish', 2017, 807),
('Mad Max Fury Road', 'Action', 'Australia', 'English', 2015, 380),
('Inception', 'Sci-Fi', 'USA', 'English', 2010, 837),
('The Revenant', 'Adventure', 'USA', 'English', 2015, 532),
('La La Land', 'Musical', 'USA', 'English', 2016, 447),
('The Secret in Their Eyes', 'Crime', 'Argentina', 'Spanish', 2009, 34),
('No Time to Die', 'Action', 'UK', 'English', 2021, 774);
'''


cursor.execute(insert_query)

cursor.execute("SELECT * FROM movies")

movies = cursor.fetchall()

movie_tuples = []

for movie in movies:
    movie_tuple = (
        movie['id'],
        movie['movie_name'],
        movie['genre'],
        movie['country'],
        movie['language'],
        movie['year'],
        movie['revenue']
    )
    movie_tuples.append(movie_tuple)


conn.close()


for movie in movie_tuples:             # to make the output more readable#
    print(f"ID: {movie[0]}")
    print(f"Movie Name: {movie[1]}")
    print(f"Genre: {movie[2]}")
    print(f"Country: {movie[3]}")
    print(f"Language: {movie[4]}")
    print(f"Year: {movie[5]}")
    print(f"Revenue: {movie[6]} million")
    print("-" * 30)

############################################################################################################# SECTION B:

import sqlite3

conn = sqlite3.connect('SQLite.exam.q4.db')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

user_input = input("Enter a part of the movie name, numbers are optional: ").lower()

cursor.execute("SELECT * FROM movies WHERE movie_name LIKE ?", ('%' + user_input + '%',))

movies = cursor.fetchall()


if movies:
    for movie in movies:
        print(f"ID: {movie['id']}")
        print(f"Movie Name: {movie['movie_name']}")
        print(f"Genre: {movie['genre']}")
        print(f"Country: {movie['country']}")
        print(f"Language: {movie['language']}")
        print(f"Year: {movie['year']}")
        print(f"Revenue: {movie['revenue']} million")
        print("-" * 30)
else:
    print("No movies found matching your search.")

conn.close()

############################################################################################################# SECTION C:

import sqlite3

conn = sqlite3.connect('SQLite.exam.q4.db')
conn.row_factory = sqlite3.Row  # To access columns by name

cursor = conn.cursor()

movie_name = input("Enter the movie name: ")
genre = input("Enter the genre: ")
country = input("Enter the country: ")
language = input("Enter the language: ")
year = int(input("Enter the release year: "))
revenue = float(input("Enter the revenue (in millions): "))


insert_query = """
INSERT INTO movies (movie_name, genre, country, language, year, revenue)
VALUES (?, ?, ?, ?, ?, ?)
"""

cursor.execute(insert_query, (movie_name, genre, country, language, year, revenue))

conn.commit()

conn.close()
















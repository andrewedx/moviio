import sqlite3

db = "database.sqlite"


movies = [
    {
        "Title": "Batman Begins",
        "Year": "2005",
        "imdbID": "tt0372784",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg"
    },
    {
        "Title": "Batman v Superman: Dawn of Justice",
        "Year": "2016",
        "imdbID": "tt2975590",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg"
    },
    {
        "Title": "The Batman",
        "Year": "2022",
        "imdbID": "tt1877830",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMDdmMTBiNTYtMDIzNi00NGVlLWIzMDYtZTk3MTQ3NGQxZGEwXkEyXkFqcGdeQXVyMzMwOTU5MDk@._V1_SX300.jpg"
    }
]


def create_table():
    conn = sqlite3.connect(db)
    print("Open database successfull\nCreating table...")
    conn.execute('''
        CREATE TABLE MOVIES
        (
            imdbID TEXT PRIMARY KEY,
            Title TEXT,
            Year TEXT,
            Type TEXT,
            Poster TEXT
        );
    
    ''')
    conn.close()
    print("Table created successfully\n")


def insert(movie):
    try:
        data = (
            movie["imdbID"],
            movie["Title"],
            movie["Year"],
            movie["Type"],
            movie["Poster"]
        )

        conn = sqlite3.connect(db)
        conn.execute(f'''
            INSERT INTO MOVIES (
            imdbID,
            Title,
            Year,
            Type,
            Poster
            )

            VALUES 
            {data}

        ''')
        conn.commit()
        conn.close()
        print("Movie inserted successfully\n")
        return "Movie inserted successfully"

    except Exception as e:
        conn.close()
        print(e)
        return e


def select():
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                imdbID,
                Title,
                Year,
                Type,
                Poster

            FROM MOVIES
            
        ''')
        raw_data = cursor.fetchall()
        conn.close()
        data = []
        for i in raw_data:
            movie_data = {
                "imdbID": i[0],
                "Title": i[1],
                "Year": i[2],
                "Type": i[3],
                "Poster": i[4]
            }
            data.append(movie_data)
        return data
    except Exception as e:
        conn.close()
        print(e)
        return e


def delete(imdbID):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(f'''
            DELETE FROM MOVIES
            WHERE imdbID = "{imdbID}"
        ''')
        conn.commit()
        conn.close()
        print("Movie deleted successfully\n")
        return "Movie deleted successfully"
    except Exception as e:
        conn.close()
        print(e)
        return e

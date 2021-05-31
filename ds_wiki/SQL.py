import sqlite3

def packages():
    return "Required packages: \n sqlite3"


def setup():
    '''Shows how to setup/enable queries from a specific database'''
    description = '''In order to query SQL databases you need to create a connection (to a database) and a cursor to that connection:'''
    conn = "conn = sqlite3.connect('path/to/data.sqlite')"
    db = "db = conn.cursor()"
    return description, conn, db


def query():
    '''Shows how to query a specific database'''
    zero = f'''0ro: {setup()}'''
    first = '''1st: query = SELECT table \n FROM database'''
    second = '''2nd: Execute with dbs.execute(query)'''
    third = '''3rd: Fetch the results with dbs.fetchall()'''
    return zero, first, second, third



def keywords():
    '''Presents keywords that can be used on queries'''
    val_dict = {
        'SELECT': 'Select which database.table to retrieve information from',
        'FROM': 'Selects which database to collect from',
        'GROUP BY': 'Aggregates a specific column',
        'HAVING': 'Used with group by to aggregate in a spcific manner',
        'ORDER BY': 'Orders on a specific manner',
        'ASC / DESC': 'Used with order by to order by ascending or descensing',
        'JOIN ... ON': 'Join a table to other table on a specific key',
        'LIMIT': 'Limit the query to n entries',
        'WHERE': 'Create a condition for the query',
        'AS': 'Give a name to something',
        'MIN / MAX': 'search the minimium or maximum value'
    }
    return val_dict



def examples():
    query1 = """SELECT 
    m.title, 
    m.genres, 
    directors.name 
FROM movies as m 
JOIN directors ON m.director_id = directors.id\n\n"""
    query2 = """SELECT 
    directors.name, 
    (MIN(m.start_year) - directors.birth_year) AS age_when_first_time_director 
FROM movies as m 
JOIN directors ON m.director_id = directors.id
GROUP BY
    directors.name
    HAVING age_when_first_time_director IS NOT NULL 
ORDER BY age_when_first_time_director ASC
LIMIT 5\n\n"""
    genre_name = 'variable inputed here'
    query3 = f"""SELECT
    directors.name, 
    count(movies.title) as count_movie
FROM movies
JOIN directors ON movies.director_id = directors.id
WHERE genres = '{genre_name}'
GROUP BY directors.name
ORDER BY count_movie desc, directors.name ASC
LIMIT 5"""
    return print(query1,query2,query3)
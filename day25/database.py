from socket import create_connection


def update_movie(movie_id:int, movie:MovieCreate) -> bool
         connection = create_connection()
         cursor = connection.cursor()
         cursor.execute("UPDATE movies SET title=?, direcor=? WHERE id=? ",(movie.title, movie.director, movie_id))
         connection.commit()
         updated = cursor.rowcount
         connection.close()
         return updated>0

def delete_movie(movie_id: int) -> bool:

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?",(movie_id))
    deleted= cursor.rowcount
    connection.close()
    return deleted>0
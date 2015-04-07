"""
Udacity Full Stack Web Developer Nanodegree
Project 1 - Movie Trailer Website
Description:
Creates a list of Movie objects and handles it to a utility function that
renders a web page with the Title, Short Description, Movie Poster and a
link to a trailer in YouTube.

"""

from movies import Movie
from fresh_tomatoes import open_movies_page

__author__ = "Henri Fontana"
__email__ = "henrif@gmail.com"

'''
List of tuples containing the information about the movies and trailers
'''
MOVIES_LIST = [("Avengers 2",
                "Bunch of super-heroes saving the world, again",
                "http://upload.wikimedia.org/wikipedia/en/1/1b/"
                "Avengers_Age_of_Ultron.jpg",
                "http://www.youtube.com/watch?v=JAUoeqvedMo"),
               ("Jurassic World",
                "Twenty-two years after the events of Jurassic Park, Isla "
                "Nublar, an island located off Central America's Pacific "
                "Coast, near Costa Rica, now features a fully functioning "
                "dinosaur theme park, Jurassic World.",
                "http://upload.wikimedia.org/wikipedia/en/6/66/"
                "JurassicWorldComicConPoster.jpg",
                "http://www.youtube.com/watch?v=RFinNxS5KN4"),
               ("Terminator Genisys",
                "In 2029, John Connor, leader of the Resistance, continues "
                "the war against the machines.",
                "http://upload.wikimedia.org/wikipedia/en/b/bc/"
                "Terminator_Genisys.JPG",
                "http://www.youtube.com/watch?v=62E4FJTwSuc"),
               ("Ted 2",
                "Ted must prove his personhood in a court of law so that "
                "he and his wife can adopt a baby.",
                "http://upload.wikimedia.org/wikipedia/en/2/24/"
                "Ted_2_poster.jpg",
                "http://www.youtube.com/watch?v=S3AVcCggRnU"),
               ("Star Wars Episode VII: The Force Awakens",
                "The Force Awakens is set approximately 30 years after the "
                "events of Return of the Jedi, and features three new leads "
                "alongside characters returning from previous Star Wars "
                "films.",
                "http://upload.wikimedia.org/wikipedia/en/2/28/"
                "Starwarsviitheforceawakens.jpg",
                "http://www.youtube.com/watch?v=7LTkgsJ1eCI"),
               ("Mad Max: Fury Road",
                "Though determined to wander the post-apocalyptic wasteland "
                "alone, Mad Max (Tom Hardy) joins Furiosa (Charlize Theron), "
                "a fugitive imperator",
                "http://upload.wikimedia.org/wikipedia/en/f/fb/"
                "Mad_Max_Fury_Road_poster.jpg",
                "http://www.youtube.com/watch?v=YWNWi-ZWL3c")]

def init_movies(list_of_movies):
    """Returns a list of Movie objects
    list_of_movies: A list of tuples in format (Movie Name, Description,
    Post image URL, Trailer Video URL)
    
    The rationale for detaching this function is to expand functionality
    (e.g. load from a text file) with minimum impact in the main code 
    """
    movies = []
    for movie_entry in MOVIES_LIST:
        movie = Movie(movie_entry[0],
                      movie_entry[1],
                      movie_entry[2],
                      movie_entry[3])
        movies.append(movie)
    return movies

if __name__ == '__main__':
    movies = init_movies(MOVIES_LIST)
    open_movies_page(movies)
    
'''
Created on Mar 25, 2015

@author: henrif
'''
import webbrowser

class Movie():
    def __init__(self, title, description, image, trailer):
        self.title = title
        self.description = description
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
        
    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)
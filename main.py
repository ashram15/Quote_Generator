import requests
import tkinter as tk
from tkinter import *
from config import API_key


# This method updates the label text to display a new quote at each method call


def update_display():

    quotes_data = get_data()

    # extracts the dictionary from the python list and ouputs the value of the "quote" key and 'author' key
    quote = quotes_data[0].get('quote')
    author = quotes_data[0].get('author')
    genre = quotes_data[0].get('category')

    # Formats quote and author into a string
    text_to_print = f"{quote} - {author}"

    # Format mood:
    genre_to_print = f"Genre is {genre.capitalize()}"

    quote_label.config(text=text_to_print)
    genre_label.config(text=genre_to_print)

# This method makes a HTTP GET request to the API Ninjas "Famous Quotes" API. It then parses the resulting JSON file to isolate the quote and author.
# Returns: A formatted string containing the quote and the author.


def get_data():

    url = "https://api.api-ninjas.com/v1/quotes"

    # Makes the HTTP Get request. The response contains JSON data formatted as an array (list) containing
    # a single dictionary object
    response = requests.get(
        url, headers={'X-Api-Key': API_key})

    # parses the JSON response into a python list containing the one dictionary
    quotes_json = response.json()

    return quotes_json


# creates popup_window
popup_window = Tk()
popup_window.title("Quote Generator")

# creates button that generates new quote on click
button = Button(popup_window, text="Quote of the day: ",
                command=update_display)
button.pack()  # displays button

# creates an actionless button that is to updated on each click for a new Quote. This button will display the quote. Its
# contents will be updated in update_display()
quote_label = Button(
    popup_window, text="Click \'Quote of the day\' to get a quote!", wraplength=500, fg="black", pady=10)
quote_label.pack(padx=10, pady=5)

genre_label = Button(popup_window, text="Genre", fg="black", pady=10)
genre_label.pack(padx=10, pady=5)

popup_window.mainloop()

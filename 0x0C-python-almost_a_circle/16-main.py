#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    Rectangle.save_to_file([Rectangle(3, 4), Rectangle(5, 8, 1), Rectangle(9, 1, 3, 2)])
#!/usr/bin/python3
"""Base class"""
import json
import os
import csv


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
            A constructor for class objects

            args:
                id (int , option) : the id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            A method that convert a list into json string

            args:
                list_dictionaries (string): the list you want to convert

            Return:
                (string) : json representation of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            A method to convert a list of Base obj into json format
            and save it inot a json file

            args:
                list_objs (Base list): list of obj you want to convert
        """
        jsonlist = [obj.to_dictionary() for obj in list_objs]

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            cls.to_json_string(jsonlist)

    @staticmethod
    def from_json_string(json_string):
        """
            A method that convert a json string to python objects
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A method to create a class instance with the given attributes"""
        if cls.__name__ == "Rectangle":
            instance = cls(10, 10)
        else:
            instance = cls(10)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
            A method that load the content of a file
            and create a class instance using the file content
        """
        file_path = f"{cls.__name__}.json"

        if not os.path.exists(file_path):
            # Decide whether to raise an exception or return a default value
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        content = cls.from_json_string(content)

        objs = []
        for item in content:
            objs.append(cls.create(**item))

        return objs

    @classmethod
    def load_from_file_csv(cls):
        """Save the content of a class instance into csv file"""
        file_path = f"{cls.__name__}.csv"

        if not os.path.exists(file_path):
            # Decide whether to raise an exception or return a default value
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            content = csv.reader(file)
            csv_content = list(content)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_content:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins

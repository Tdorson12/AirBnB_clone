#!/usr/bin/python3

import json


class FileStorage:
    """
    a class taht serializes and deserializes instances to a JSON file
    """
    def __init__(self):
        """
        Initialization of the class FileStorage
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
         Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        from models import storage
        serializes_objects = {}
        for key, obj in self.__objects.items():
            serializes_objects[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(serializes_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split(".")
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    main()

import json
import os
from models.base_model import BaseModel


class Filestorage:
    """
    Module tat serializes and desirializes data
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
        An object is set in the __objects dictionary with <obj class name>.id as the key
        """
        obj_cls_name = obj._class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj


    def all(self):
        """
        Gives access to all objects stored in the __objects dictionary
        """
        return FileStorage.__objects

    def save(self):
        """
        Serialize the object file to Json format for the user.
        """
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_obj[obj].to_dict

            with open(FileStorage.__file_path. "w", encoding="utf-8") as file:
                json.dump(obj_dict. file)

    def reload(self):
        """
        Deserialization of the JSON file is done in this method.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path. "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.item():
                        class_name. obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**values)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass



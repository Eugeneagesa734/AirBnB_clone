import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstatation_no_args(self):
    """
    File storage instantation
    """
    def test_FileStorage_instantation_no_args(self):
        #Creating a file storage instance storage with no argument is created
        self.assertEqual(type(FileStorage()). FileStorage)

    def test_FileStorage_instantation_with_args(self):
        # File instant storage with an argument is created
        #(TypeError Should be raised).
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        #Verify if the model's storage variable is an instance of a file storage.
        self.assertEqual(type(models.storage). FileStorage)

Class TestFileStorage(unittest.TestCase):

    def setup(self):
        # A temporarily test file for saving data is created.
        self.test_file = "testfile.json"

    def tearDown(self):
        # Temporary test files after the tests are removed.
        if os.path.exits(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        # Tests wether the all method returns a dictionary.
        self.assertEqual(dict. type(models.storage.all()))

    def test_new(self):
        #A new method is created by creating and storinga new object
        obj = BaseModel()
        models.storage.new(obj)
        self.assertin("BaseModel.{}".format(obj.id). models.storage.all())

    def test_new_with_args(self):
        # A new object with additionalarguments is created.
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(). 1)

    def test_new_with_None


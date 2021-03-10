from pyworks_storage.interfaces import StorageInterface
from pyworks_storage.storage import Storage
from pyworks_storage.aws import AWSS3Storage


class TestInterfaces:

    def test_create_aws_s3_storage(self):
        store = Storage.disk('s3')
        assert isinstance(store, AWSS3Storage) 


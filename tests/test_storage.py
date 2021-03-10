import pytest
from utils import download_image
from pyworks_storage.storage import Storage


# Prepare something ahead of all tests    
@pytest.fixture(scope="session", autouse=True)
def setup(request):
    download_image()

class TestStorage:

    def test_put_image(self):
        store = Storage.disk('s3')
        file_path = 'avatar.png'
        uploaded_link = store.put_image(file_path=file_path)
        assert 's3.amazonaws.com' in  uploaded_link
        assert 'avatar.png' in  uploaded_link

import requests
import shutil


def download_image():
    image_url = "https://avatars.githubusercontent.com/u/60771858"
    filename = "avatar.png"
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception

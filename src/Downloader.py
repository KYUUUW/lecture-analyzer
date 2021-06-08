import urllib.request

class Downloader:
    """
    lecture: [("lecture_name": string, "code": string), ...]
    """
    def __init__(self, lectures):
        self.lectures = lectures
        self.downloaded = []

    def download_all(self, dirname):
        for lecture_name, url in self.lectures:
            print(f'Downloading {lecture_name} from [{url}]')

            download_path = f'{dirname}/{lecture_name}.mp4'
            try:
                urllib.request.urlretrieve(url, download_path)
            except:
                print(f'Downloading {lecture_name} failed!!!')
                self.downloaded.append(download_path)

        return self.downloaded
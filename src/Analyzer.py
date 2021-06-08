from Capture import Capture
from Downloader import Downloader
from PdfComposer import PdfComposer
import os
import json

class Analyzer:
    def __init__(self, lectures: [tuple], threshold = 4.0):
        self.lectures = lectures
        self.threshold = threshold

    def analyze(self):
        video_path = os.path.abspath('../data/videos')
        capture_path = os.path.abspath('../data/captures')
        pdf_path = os.path.abspath('../result/lecture.pdf')

        Downloader(self.lectures).download_all(video_path)
        Capture(video_path, capture_path, self.threshold).get_all_scene()
        PdfComposer(capture_path, pdf_path).compose()


if __name__=='__main__':
    codes = json.load(open('../assets/lecture_codes.json')).items()

    lectures = []
    for name, code in codes:
        url = f'https://sejong.commonscdn.com/contents2/sejongl101/{code}/contents/media_files/mobile/ssmovie.mp4'
        lectures.append((name, url))

    # name = '13-02'
    # url = f'https://sejong.commonscdn.com/contents2/sejongl101/6017a14cfff0d/contents/media_files/mobile/ssmovie.mp4'
    # lectures = [(name, url)]

    analyzer = Analyzer(lectures)
    analyzer.analyze()

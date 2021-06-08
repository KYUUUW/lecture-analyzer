import os
from PIL import Image

class PdfComposer:
    def __init__(self, images_dir: str, dest: str):
        self.images_dir = images_dir
        self.dest = dest

    def compose(self):
        names = os.listdir(self.images_dir)
        print(names)

        names.sort()
        print(names)

        paths = []
        for name in names:
            paths.append(f'{self.images_dir}/{name}')

        imgs = []
        for path in paths:
            if path.find('.jpg') == -1:
                continue

            imgs.append(Image.open(path).convert('RGB'))

        imgs[0].save(f'{self.dest}', save_all=True, append_images=imgs)

if __name__ == '__main__':
    PdfComposer('../data/captures', '../result/test.pdf').compose()
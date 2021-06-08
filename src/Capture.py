import cv2
import os
from scenedetect import VideoManager
from scenedetect import SceneManager
from scenedetect import FrameTimecode
from scenedetect.detectors import ContentDetector

class Capture:
    def __init__(self, video_dir: str, dest: str, threshold: float):
        self.video_dir = video_dir
        self.threshold = threshold
        self.dest = dest

    def get_frames(self, path: str):
        """
        get scenes for video
        :param path: path to video
        :return: frames of scene
        """

        # Create our video & scene managers, then add the detector.
        video_manager = VideoManager([path])
        scene_manager = SceneManager()
        scene_manager.add_detector(
            ContentDetector(threshold=self.threshold))

        # Improve process
        # sing speed by downscaling before processing.
        video_manager.set_duration(start_time=FrameTimecode(500, 15))
        video_manager.set_downscale_factor()

        # Start the video manager and perform the scene detection.
        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)
        scenes = scene_manager.get_scene_list()

        frames = []
        for frame in scenes:
            frames.append(frame[0].frame_num + 50)

        # Remove useless last frame
        frames = frames[0: len(frames) - 1]
        return frames

    def get_images(self, path: str, frames: [int]):
        """
        Get images of frames in video
        :param path: path to video
        :param frames: frmaes to get image
        :return: images of fraems
        """

        # Read the video from specified path
        cam = cv2.VideoCapture(path)

        try:

            # creating a folder named data
            if not os.path.exists(f'{self.dest}/frames'):
                os.makedirs(f'{self.dest}/frames')

        # if not created then raise error
        except OSError:
            print('Error: Creating directory of data')

        # frame
        for currentframe in frames:
            # reading from frame
            cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)
            ret, frame = cam.read()

            if ret:
                # if video is still left continue creating images
                video_name = os.path.basename(path)
                name = f'{self.dest}/{video_name}-{"{:05d}".format(currentframe)}.jpg'

                # writing the extracted images
                cv2.imwrite(name, frame)
                print('Creating...' + name)

                # increasing counter so that it will
                # show how many frames are created
            else:
                print(f'{currentframe} frame extract fail')

        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()
        return f'{self.dest}'

    def get_all_scene(self):
        names = os.listdir(self.video_dir)
        paths = []
        for n in names:
            if n.find('.mp4') == -1:
                continue
            paths.append(f'{self.video_dir}/{n}')

        images_path = ''
        for path in paths:
            frames = self.get_frames(path)
            images_path = self.get_images(path, frames)

        return images_path

if __name__ == '__main__':
    video_dir = os.path.abspath('../data')
    dest = os.path.abspath('../result')
    capture = Capture(video_dir, dest, 4.0)
    print(capture.get_all_scene())

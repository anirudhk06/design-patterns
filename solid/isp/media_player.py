from abc import ABC, abstractmethod


class AudioPlayable(ABC):
    @abstractmethod
    def play_audio(self):
        pass


class VideoPlayable(ABC):
    @abstractmethod
    def play_video(self):
        pass


class AudioRecordable(ABC):
    @abstractmethod
    def record_audio(self):
        pass


class MusicPlayer(AudioPlayable):
    def play_audio(self):
        print("Playing music")


class VideoPlayer(AudioPlayable, VideoPlayable):
    def play_audio(self):
        print("Playing video audio")

    def play_video(self):
        print("Playing video")


class VoiceRecorder(AudioRecordable):
    def record_audio(self):
        print("Recording audio")

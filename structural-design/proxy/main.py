from abc import ABC, abstractmethod


class VideoServiceInterface(ABC):
    @abstractmethod
    def play_video(self, user_type: str, video_name: str):
        pass


class VideoService(VideoServiceInterface):
    def play_video(self, user_type: str, video_name: str):
        print(f"Streaming video {video_name}")


class ProxyVideoService(VideoServiceInterface):
    def __init__(self, video_service: VideoService):
        self.video_service = video_service

    def play_video(self, user_type, video_name):

        if user_type != "premium":
            print("Access denied")
            return

        self.video_service.play_video(user_type, video_name)


def main() -> None:
    service = ProxyVideoService(VideoService())
    service.play_video("premium", "Learn LLD")


if __name__ == "__main__":
    main()

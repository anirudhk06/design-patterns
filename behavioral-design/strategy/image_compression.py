from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress(self, file_name: str) -> None:
        pass


class JpegCompressor(Compressor):
    def compress(self, file_name) -> None:
        print(f"Compressing {file_name} using JPEG")


class PngCompressor(Compressor):
    def compress(self, file_name) -> None:
        print(f"Compressing {file_name} using PNG")


class WebpCompressor(Compressor):
    def compress(self, file_name) -> None:
        print(f"Compressing {file_name} using WEBP")


class ImageProcessor:
    def __init__(self, file_name: str = None, compressor: Compressor = None) -> None:
        self.file_name = file_name
        self.compressor = compressor

    def compress(self) -> None:
        if self.file_name is None:
            raise ValueError("Image must be set.")

        if self.compressor is None:
            raise ValueError("Image compressor not set.")
        self.compressor.compress(self.file_name)

    def set_compressor(self, compressor: Compressor) -> None:
        if not isinstance(compressor, Compressor):
            raise ValueError("Invalid compressor")
        self.compressor = compressor


def main() -> None:
    processor = ImageProcessor("header.jpg", WebpCompressor())
    processor.compress()

    processor.set_compressor(PngCompressor())
    processor.compress()


if __name__ == "__main__":
    main()

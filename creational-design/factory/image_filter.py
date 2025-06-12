from typing import Type


class ImageFilter:
    def apply(self, *args, **kwargs) -> None:
        raise NotImplementedError("Subclasses must be implemented apply method")


class BlackWhiteFilter(ImageFilter):
    def apply(self, image: str) -> None:
        print(f"Applied Black & White filter to image: {image}")


class SepiaFilter(ImageFilter):
    def apply(self, image: str) -> None:
        print(f"Applied Sepia filter to image: {image}")


class BlurFilter(ImageFilter):
    def apply(self, image: str) -> None:
        print(f"Applied Blur filter to image: {image}")


class ImageFilterFactory:
    _methods: dict[str, Type[ImageFilter]] = {
        "blackwhite": BlackWhiteFilter,
        "sepia": SepiaFilter,
        "blur": BlurFilter,
    }

    @staticmethod
    def get_filter(filter: str = None) -> ImageFilter:
        """
        Supported filters:
        - black_and_white
        - sepia
        - blur
        """

        clean_filter: str = str(filter).lower().strip()

        if clean_filter not in ImageFilterFactory._methods:
            raise ValueError(
                f"Invalid filter of {filter}. Supported filters are {', '.join([key for key in ImageFilterFactory._methods.keys()])}"
            )

        return ImageFilterFactory._methods[clean_filter]()


def main() -> None:
    filter_obj = ImageFilterFactory.get_filter("blackwhite")
    filter_obj.apply("profile.png")


if __name__ == "__main__":
    main()

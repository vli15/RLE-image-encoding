import heifer_generator
class Cow:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def get_image(self):
        return self._image

    def set_image(self, _image):
        self._image = _image
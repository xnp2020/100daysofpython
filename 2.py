class Screen(object):
    def __init__(self):
        self._width = width
        self._height = height
        self._resolution = self.width * self.height

    @property
    def width(self):
       return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._resolution

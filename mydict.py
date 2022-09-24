class Dict(dict):
    """自定义字典实现属性功能"""

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s' % attr")

    def __setattr__(self, key, value):
        self[key] = value

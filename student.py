class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def name(self):
        return self.__name

    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('score must between 0~100!')
        else:
            if self.score >= 80:
                return 'A'
            elif self.score >= 60:
                return 'B'
            return 'C'

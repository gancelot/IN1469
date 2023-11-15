import abc
import weakref


class ReadOnly:
    def __init__(self):
        self.data = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, '(no title)')

    def __set__(self, instance, value):
        if not self.data.get(instance):
            self.data[instance] = value


class Media(abc.ABC):
    title = ReadOnly()

    @abc.abstractmethod
    def __init__(self, title: str = '', release_date: str = ''):
        self.title = title
        self.release_date = release_date

    def __str__(self):
        return f'{self.title} ({self.release_date})'


class Movie(Media):
    def __init__(self, title: str = '', release_date: str = '', revenue: int = 0, runtime: int = 0,
                 tagline: str = '', budget: int = 0, **extras):
        super().__init__(title, release_date)
        self.revenue = revenue
        self.runtime = runtime
        self.tagline = tagline
        self.budget = budget
        self.extras = extras

    def __str__(self):
        return f'{super().__str__()}, revenue: {self.revenue}, budget: {self.budget}'


if __name__ == '__main__':
    m = Movie('Titanic')
    m.title = 'Spider-man'
    print(m)

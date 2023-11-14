from contextlib import closing


class Foo:
    def shutdown(self):
        print('in shutdown')


class ClosingFoo(Foo):
    def close(self):
        super().shutdown()


with closing(ClosingFoo()):
    print('in with')
class Foo:
    bar = "A"

    def __init__(self):
        self.bar = 'B'

    class Bar:
        bar = 'C'

        def __init__(self):
            self.bar = 'D'


print(Foo.bar)       # A 출력
print(Foo().bar)     # B 출력
print(Foo.Bar.bar)   # C 출력
print(Foo.Bar().bar)  # D 출력

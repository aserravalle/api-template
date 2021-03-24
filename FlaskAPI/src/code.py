

class Code:
    def __init__(self):
        self.hello_txt = "Hello {fname}!"

    def hello(self, name: str) -> str:
        return self.hello_txt.format(fname = name)

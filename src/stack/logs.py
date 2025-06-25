class Log:
    def __init__(self, content):
        content = content.replace(' ', '')
        content = content.split(":")
        self.id = int(content[0])
        self.is_start = content[1] == "start"
        self.time = int(content[2])

    def __str__(self):
        return "id:{} is_start:{} time:{}".format(self.id, self.is_start, self.time)
from bot import Bot

class Command:

    def __init__(self, command, check):
        self.receiver = None
        self.receiverlow = None
        self.receiverhigh = None
        self.ejector = None
        self.value = None
        self.command = command.split()
        self.check = check
        self.analyze()
        self.execute()

    def __repr__(self):
        return " ".join(self.command)

    def analyze(self):
        if self.command[0] == "value":
            self.receiver = self.get_create_bot(f"{self.command[-2]} {self.command[-1]}")
            self.value = int(self.command[1])
        else:
            self.ejector = self.get_create_bot(f"{self.command[0]} {self.command[1]}")
            self.receiverlow = self.get_create_bot(f"{self.command[5]} {self.command[6]}")
            self.receiverhigh = self.get_create_bot(f"{self.command[-2]} {self.command[-1]}")

    def execute(self):
        if self.value:
            self.receiver.add_command(["receive", [self.value]])
        else:
            self.ejector.add_command(["give", [self.receiverlow, "low"]])
            self.ejector.add_command(["give", [self.receiverhigh, "high"]])

    def get_create_bot(self, name):
        bots = Bot.bots
        bot = bots.get(name)
        if not bot:
            bot = Bot(name, self.check)
        return bot
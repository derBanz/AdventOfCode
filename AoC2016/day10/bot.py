class Bot:
    bots = dict()
    winner = None

    def __init__(self, name, check):
        self.name = name
        self.check = check
        self.tokens = []
        self.commands = []
        self.bots[name] = self

    def __repr__(self):
        return self.name

    def sort_tokens(self):
        self.tokens.sort()

    def receive_token(self, parameters):
        token = parameters[0]
        self.tokens.append(token)
        self.sort_tokens()
        self.execute_commands()

    def give_token(self, parameters):
        other = parameters[0]
        token = parameters[1]
        print(self.name, self.tokens)
        if token == "low":
            other.add_command(["receive", [self.tokens.pop(0)]])
        else:
            other.add_command(["receive", [self.tokens.pop()]])

    def add_command(self, command):
        if command[0] == "receive":
            self.receive_token(command[1])
        else:
            self.commands.append(command)
            self.execute_commands()

    def execute_command(self):
        command = self.commands.pop(0)
        self.give_token(command[1])

    def execute_commands(self):
        if len(self.tokens) > 1:
            if self.tokens[0] in self.check and self.tokens[1] in self.check:
                Bot.winner = self
            while len(self.commands) > 0 and len(self.tokens) > 0:
                self.execute_command()
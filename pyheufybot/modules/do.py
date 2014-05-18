from pyheufybot.module_interface import Module, ModuleType

class ModuleSpawner(Module):
    def __init__(self, bot):
        self.bot = bot
        self.name = "Do"
        self.trigger = "do"
        self.moduleType = ModuleType.COMMAND
        self.messageTypes = ["PRIVMSG"]
        self.helpText = "Usage: do <message> | Makes the bot perform the given action."

    def execute(self, message):
        if len(message.params) == 1:
            self.bot.msg(message.replyTo, "Do what?")
        else:
            self.bot.action(message.replyTo, " ".join(message.params[1:]))

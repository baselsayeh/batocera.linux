import os

from ... import Command
from ..Generator import Generator

class PygameGenerator(Generator):

    def generate(self, system, rom, playersControllers, metadata, guns, wheels, gameResolution):
        commandArray = ["pygame", rom]
        return Command.Command(array=commandArray)

    def executionDirectory(self, config, rom):
        return os.path.dirname(rom)

    def getInGameRatio(self, config, gameResolution, rom):
        return 16/9

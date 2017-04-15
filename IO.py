class IO:
    #Class Input-Output for working with files

    def read(self, path):
        fIn = open(path, "r")
        lines = fIn.read().splitlines()
        fIn.close()
        return lines

    def write(self, path, output):
        self.fOut = open(path, "w+")
        self.fOut.write(output)
        self.fOut.close()


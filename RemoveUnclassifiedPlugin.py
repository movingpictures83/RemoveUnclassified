import sys


class RemoveUnclassifiedPlugin:
    def input(self, filename):
       infile = open(filename, 'r')
       self.lines = []
       for line in infile:
           if not "unclassified" in line:
               self.lines.append(line)

    def run(self):
        for i in range (0, len(self.lines)):
            contents = self.lines[i].strip().split('\t')
            taxon = contents[0]
            taxonomy = taxon.split('|')
            if (len(taxonomy) == 7):
               species = taxonomy[6]
               genus = taxonomy[5]
               self.lines[i] = self.lines[i].replace(species, genus+'_'+species)

    def output(self, filename):
        outfile = open(filename, 'w')
        for line in self.lines:
            outfile.write(line)


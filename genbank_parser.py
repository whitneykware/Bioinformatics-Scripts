import re
print("Whitney Ware"+'\n'+"wwware4@uncc.edu"+'\n')

infile = "hw2_hla.gb.txt"

class GenBankEntry:
    info = {}
    geneSeq = []
    aminoAcidSeq = []
    def __init__(self, file):
        with open(infile, "r") as file:
            for line in file.readlines():
                if line.startswith('ACCESSION'):
                    cols = line.rstrip().split()
                    self.info['Accession']= cols[1]
                elif line.startswith('SOURCE'):
                    cols = line.rstrip().split()
                    self.info['Organism'] = str.join(' ', (cols[1:]))
                elif line.startswith('VERSION'):
                    cols = line.rstrip().split(':')
                    self.info['GI'] = cols[1]
                elif re.search(r'^\s*(/gene)', line):
                    cols = line.rstrip().split("=")
                    self.info['Gene'] = cols[1]
                elif re.search(r'^\s*\d+', line):
                    for i in line:
                        if not i.isdigit():
                            self.geneSeq.append(i.rstrip())
                    self.info['Sequence'] = "".join(self.geneSeq)
                elif re.search(r'^(\s+/translation=")|^(\s+[A-Z]+)+([A-Z]+\S?\w*)$', line):
                    for i in line:
                        if i.isupper():
                            self.aminoAcidSeq.append(i.rstrip())
                    self.info['Amino Acid Sequence'] = "".join(self.aminoAcidSeq)

    def __str__(self):
        return 'GenBankEntry Organism: {}'.format(self.info['Organism'])

    def __repr__(self):
        return "<GenBankEntry {} {} '{}'>".format(self.info['GI'], self.info['Accession'], self.info['Organism'])

    def get_entry_value(self, key):
        if key in self.info.keys():
            print(key + ': ' + self.info[key])
        else:
            print(key + ' is not found.')

    def display_entry(self):
        for key, value in self.info.items():
           print(key + ': ' + str(value))


#examples
gen_entry = GenBankEntry(infile)
gen_entry.display_entry()
print(gen_entry)
gen_entry.get_entry_value('GI')
gen_entry.get_entry_value('notKey')


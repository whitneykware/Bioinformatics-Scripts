#input file: hw3.vcf
#output file: hw3.vcf.out

class Vcf:
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return 'VCF file: {}' .format(self.filename)

    def parse(self):
        with open(self.filename, 'r') as infile:
            with open(self.filename+'.out', 'w') as outfile:
                for line in infile.readlines():
                    if line.startswith('##'):
                        continue
                    if line.startswith('#'):
                        header = line.split()
                        print('ID\tCoordinate\tREF\tAlT', '\t'.join(header[9:]), sep='\t', file=outfile)
                        continue
                    if not line.strip():
                        continue
                    col = line.split('\t')
                    ID = col[2]
                    chr = col[0]
                    pos = col[1]
                    coord = "chr" + chr + ":" + pos
                    ref = col[3]
                    alt = col[4]
                    genotype = col[9:]
                    genotype = [i.split(':', 1)[0] for i in genotype]
                    print(ID + '\t' + coord + '\t' + ref + '\t' + alt + '\t' + '\t'.join(map(str,genotype)), file=outfile)

hw3 = Vcf('hw3.vcf')
hw3.parse()
print(hw3)


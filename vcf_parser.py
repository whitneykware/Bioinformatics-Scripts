#input file:hw5.vcf
#output file: hw5.bed

with open('hw5.vcf', 'r') as vcf:
    with open('hw5.bed', 'w') as outfile:
        for line in vcf.readlines():
            line = line.rstrip()
            if line.startswith('##'):
                continue
            if line.startswith('#'):
                fields = line.split('\t')
                print("Chrom\tStart\tEnd\tLength\tSVType\tHG00514", file=outfile)
                continue
            fields = line.split('\t')
            chrom = fields[0][-1]
            start = fields[1]
            info = fields[7]
            cols = info.split(';')
            end = cols[0][4:]
            length = cols[2][6:]
            svtype = cols[1][7:]
            sample = fields[9]
            output = chrom + '\t' + start + '\t' + end + '\t' + length + '\t' + svtype + '\t' + sample
            print(output, file=outfile)

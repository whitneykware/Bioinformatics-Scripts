def gene_list(file):
        file+=line.strip().split('\n')

l = []
with open('sample_genes') as x:
        for line in x:
                gene_list(x)

def expression_dic(file):
        fields = line.split()
        name = fields[0]
        expression = fields[4:]
        g[name] = expression

g = {}
with open('gene_expression_100') as f:
                header=f.readline()	
                for line in f:
                        expression_dic(f)


for i in l:
        print(i,g[i])



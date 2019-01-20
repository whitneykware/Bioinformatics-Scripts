import sys
def gene_list(x):
        genes = []
        genes = x.read().splitlines()
        return genes

def expression_dic(y):
        g = {}
        header = y.readline()
        for line in y:
                fields = line.split()
                name = fields[0]
                expression = fields[4:]
                g[name] = expression
        return g

def final(list,dic):
        for i in list:
                print (i, dic[i])
                
with open("sample_genes") as f:
        with open("gene_expression_100") as f2:
                final(gene_list(f),expression_dic(f2))

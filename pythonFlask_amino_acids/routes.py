from app import app
from flask import make_response
@app.route('/')
@app.route('/index')
def index():
	amino_acids = ['Alanine', 'Arginine', 'Asparagine', 'Aspartic Acid', 'Cysteine', 'Glutamine', 'Glutamic Acid',
               'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine',
               'Proline', 'Serine', 'Threonine', 'Tryptophan', 'Tyrosine', 'Valine']

	letter = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

	aa_dict = dict(zip(amino_acids, letter))
	result = '<br/>'.join(['The one letter abbreviation of {} is {}.'.format(key, value) for (key, value) in aa_dict.items()])
	return result
	

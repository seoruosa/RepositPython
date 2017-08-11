# -*- coding: UTF-8 -*-

class Schema(object):
	'''Objeto para armazenar e identificar o schema'''
	schemaList = {}

	def __init__(self, schemaName):
		self.schemaName = schemaName

	def addSchema(self, attrName, attribute, attrQuant):
		self.schemaList[attrName] = [attribute, attrQuant]

	def retQuant(self, attrName):
		return self.schemaList[attrName][1]

def actualFacts(factsTable, schemaTable):
	
	endTel = Schema('endTel')
	for s in schema:
		endTel.addSchema(s[0],s[1],s[2])

	currentFacts={}

# Utiliza um dicionario onde a chave sao os enderecos e numeros de telefone
	for f in facts:
		if f[3] == False:
			del currentFacts[f[2]]
		elif endTel.retQuant(f[1]) == 'many':
			currentFacts[f[2]] = [f[0], f[1], f[3]]
		else:
			for key in currentFacts.keys():
				if currentFacts[key][0] == f[0] and currentFacts[key][1] == f[1]:
					del currentFacts[key]
					currentFacts[f[2]] = [f[0], f[1], f[3]]
					break
			else:
				currentFacts[f[2]] = [f[0], f[1], f[3]]

# Transforma o dicionario em uma tabela
	a=[]
	for key in currentFacts.keys():
		a.append([currentFacts[key][0],
		currentFacts[key][1],
		key,
		currentFacts[key][2]])

	return a

def factPrint(factsTable):
	for f in factsTable:
		print f[0] + '	',
		print f[1] + '	',
		print f[2] + '	',
		print f[3]
	print ''

#------------------------------------------------------#
facts = [
  ['gabriel', 'endereço', 'av rio branco, 109', True],
  ['joão', 'endereço', 'rua alice, 10', True],
  ['joão', 'endereço', 'rua bob, 88', True],
  ['joão', 'telefone', '234-5678', True],
  ['joão', 'telefone', '91234-5555', True],
  ['joão', 'telefone', '234-5678', False],
  ['gabriel', 'telefone', '98888-1111', True],
  ['gabriel', 'telefone', '56789-1010', True],
]

schema = [
    ['endereço', 'cardinality', 'one'],
    ['telefone', 'cardinality', 'many']
]

actual = actualFacts(facts, schema)

factPrint(facts)

print 'Após execução da função'
factPrint(actual)




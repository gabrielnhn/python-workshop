# Uma pesquisa foi realizada para ver quais eram os cursos dos alunos do projeto Yapira.
# Com base na lista de respotas obtidas abaixo, imprima uma lista que contem apenas uma vez
# cada curso obtido pela pesquisa
cursos = ['Ciência da Computação', 'Ciência da Computação', 'Engenharia Mecânica', 'Engenharia Mecânica', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Ciência da Computação', 'Ciência da Computação', 'Ciência da Computação', 'Engenharia de Produção', 'Engenharia Mecânica', 'Engenharia Elétrica', 'Ciência da Computação', 'Engenharia de Produção', 'Ciência da Computação', 'Engenharia Elétrica','Engenharia Elétrica', 'Engenharia Elétrica','Engenharia de Produção', 'Ciência da Computação']

print(list(set(cursos)))

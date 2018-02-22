import random
from decimal import Decimal

import GeneticAlgorithm as ga

# 遺伝子情報の長さ
GENOM_LENGTH = 500
# 遺伝子集団の大きさ
MAX_GENOM_LIST = 100
# 遺伝子選択数
SELECT_GENOM = 20
# 個体突然変異確立
INDIVIDUAL_MUTATION = 0.5
# 遺伝子突然変異確立
GENOM_MUTATION = 0.5
# 世代数
MAX_GENERATION = 20000

def create_genom(length):
	"""ランダムに遺伝子の作成"""
	genom_list = list()
	for i in range(length):
		genom_list.append(random.randint(0, 1))
	return ga.genom(genom_list, 0)

def evaluation(ga):
	"""評価"""
	genom_total = sum(ga.getGenom())
	return Decimal(genom_total) / Decimal(GENOM_LENGTH)

def select(ga, elite):
	"""エリートの選択"""
	sort_result = sorted(ga, reverse=True, key=lambda u: u.evaluation)
	result = [sort_result.pop(0) for i in range(elite)]
	return result

def crossover(ga_one, ga_second):
	"""交叉"""
	genom_list = list()
	cross_one = random.randint(0, GENOM_LENGTH)
	cross_second = random.randint(cross_one, GENOM_LENGTH)
	# 遺伝子の取得
	one = ga_one.getGenom()
	second = ga_second.getGenom()
	# 交叉
	progeny_one = one[:cross_one] + second[cross_one:cross_second] + one[cross_second:]
	progeny_second = second[:cross_one] +one[cross_one:cross_second] + second[cross_second:]
	genom_list.append(ga.genom(progeny_one, 0))
	genom_list.append(ga.genom(progeny_second, 0))
	return genom_list

def next_generation_gene_create(ga, ga_elite, ga_progeny):
	"""世代交代"""
	next_generation_gene = sorted(ga, reverse=False, key=lambda u: u.evaluation)
	for i in range(0, len(ga_elite) + len(ga_progeny)):
		next_generation_gene.pop(0)
	next_generation_gene.extend(ga_elite)
	next_generation_gene.extend(ga_progeny)
	return next_generation_gene

def mutation(ga, individual_mutatiion, genom_mutation):
	ga_list = list()
	for i in ga:
		if individual_mutatiion > (random.randint(0, 100) / Decimal(100)):
			genom_list = list()
			for i_ in i.getGenom():
				if genom_mutation > (random.randint(0, 100) / Decimal(100)):
					genom_list.append(random.randint(0, 1))
				else:
					genom_list.append(i_)
			i.setGenom(genom_list)
			ga_list.append(i)
		else:
			ga_list.append(i)
	return ga_list

if __name__ == '__main__':
	current_generation_individual_group = list()
	for i in range(MAX_GENOM_LIST):
		current_generation_individual_group.append(create_genom(GENOM_LENGTH))
	
	for count_ in range(1, MAX_GENERATION + 1):
		for i in range(MAX_GENOM_LIST):
			evaluation_result = evaluation(current_generation_individual_group[i])
			current_generation_individual_group[i].setEvaluation(evaluation_result)
		elite_genes = select(current_generation_individual_group, SELECT_GENOM)
		progeny_gene = list()
		for i in range(0, SELECT_GENOM):
			progeny_gene.extend(crossover(elite_genes[i - 1], elite_genes[i]))
		next_generation_individual_group = next_generation_gene_create(current_generation_individual_group,
										   elite_genes, progeny_gene)
		next_generation_individual_group = mutation(next_generation_individual_group, INDIVIDUAL_MUTATION, GENOM_MUTATION)

		fits = [i.getEvaluation() for i in current_generation_individual_group]

		min_ = min(fits)
		max_ = max(fits)
		avg_ = sum(fits) / Decimal(len(fits))

		print("-----第{}世代の結果-----".format(count_))
		print("  Min:{}".format(min_))
		print("  Max:{}".format(max_))
		print("  Avg:{}".format(avg_))
		current_generation_individual_group = next_generation_individual_group
	print("Result : {}".format(elite_genes[0].getGenom()))

# -*- coding: utf-8 -*-

def get_factors_from_number(num):
	list_factors = []
	for index in range(1, num + 1):
		if num % index == 0:
			list_factors.append(index)
	return list_factors
	

test_dict = {'Gfg' : 3,'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'}
K = 7
print("The original test_dictionary is : " + str(test_dict))
res = {}
for key in test_dict:
	if not (isinstance(test_dict[key], int) and test_dict[key] > K):
		res[key] = test_dict[key]
print("The constructed test_dictionary : " + str(res))
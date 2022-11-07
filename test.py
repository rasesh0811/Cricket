import numpy
x = [[2,3,4],[5,6,7]]
print(x)
y = numpy.transpose(x).tolist()
print(y)
print(type(x))
print(type(y))


# import pickle
# teams1 = {}
# a = {'hello': 'world'}
# def initTeamObjects():
#   '''Initialising Team Objects'''
#   try:
#     with open('teams_data.pickle', 'rt') as f:
#       teams1 = pickle.load(f)
#   except FileNotFoundError:
#     print("File DNE, teams object at present:"+str(teams))
#     with open('teams_data.pickle', 'wt') as f:
#       pickle.dump(teams, f, protocol=pickle.HIGHEST_PROTOCOL)
#       teams1 = pickle.load(f)
#   finally:
#     print("teams1:"+str(teams1))
#     # f.close()
# initTeamObjects()
# with open('teams_data.pickle', 'wb') as handle:
#     pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('teams_data.pickle', 'rb') as handle:
#     b = pickle.load(handle)

# print(a == b)
# print(b)
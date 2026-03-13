for i,j,z in zip(range(1,6), range(5,0,-1), range(10,15)):
    if i == 3 and j == 3 and z == 12:
        continue
    print(i,j,z)
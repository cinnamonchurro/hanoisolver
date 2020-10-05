def move(f, t) : 
    print('Move from {} to {}'.format(f, t))

def hanoisolver(d, s, i, e) : 
    #d = number of disks
    #s = starting position
    #i = intermediate position
    #e = ending position
    if d == 0 : 
        pass
    else : 
        hanoisolver(d-1, s, e, i)
        move(s, e)
        hanoisolver(d-1, i, s, e)

#def hanoisolver(t=3,r=8) : 
    #n is the number of towers and r is the number of disks
#    towerd = {}
#    for tc in range(t) : 
#       towerd['tower'+str(tc)] = []
#        #print(tower)
#    for rc in range(r) :
#        towerd['tower0'].append(rc)
#    print(towerd)
#    if towerd['tower0'][-1]

hanoisolver(5, 'a', 'b', 'c')
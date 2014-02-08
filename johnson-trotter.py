import math


def jt(number):
    perm = [{'num':i,'dir':'l'} for i in range(1,number+1)]
    perm_list = [[i['num'] for i in perm]]
    has_mobile_element = True
    while has_mobile_element:
        k = largest_mobile_element(perm)
        perm = swap(perm, k)
        for element in perm:
            if element['num'] > k['num']:
                if element['dir'] == 'r':
                    element['dir'] = 'l'
                else:
                    element['dir'] = 'r'
        perm_list.append([i['num'] for i in perm])
        if not largest_mobile_element(perm):
            has_mobile_element = False
    return perm_list


def swap(perm, k):
    idx = perm.index(k)
    if k['dir'] == 'r':
        perm[idx], perm[idx+1] = perm[idx+1], perm[idx]
    else:
        perm[idx], perm[idx-1] = perm[idx-1], perm[idx]
    return perm


def largest_mobile_element(permutation):
    mobile_elements = []
    for i in range(len(permutation)):
        #check the element the arrow points to if it's smaller than it's mobile
        if permutation[i]['dir'] == 'r' and  i+1 < len(permutation):
            if permutation[i+1]['num'] < permutation[i]['num']:
                mobile_elements.append(permutation[i])
        if permutation[i]['dir'] == 'l' and i-1 >= 0:
            if permutation[i-1]['num'] < permutation[i]['num']:
                mobile_elements.append(permutation[i])
    if len(mobile_elements) > 0:
        max = mobile_elements[0]
    else:
        return False
    for element in mobile_elements:
        if element['num'] > max['num']:
            max = element
    return max


def all_permutations_unique(perms): #Verify that all permutations created are unique
    if len(perms) == len([list(x) for x in set(tuple(x) for x in perms)]):
        return True
    else:
        return False


def main():

    for i in range(2,10):
        perms = jt(i)
        print "\n****TESTING: " + str(i) + "***"
        print "All Permutations Unique: " + str(all_permutations_unique(perms))
        # verify that the number of permutations actual matches n!...
        print "Number of Permutations = " + str(len(perms)) + ", " + str(i) + "!= " + str(math.factorial(i))
main()
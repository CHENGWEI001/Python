def get_finger_table(nodes, m, nodeIdx):
    finger_table = []
    nodeVal = nodes[nodeIdx]
    for i in range(m):
        tgt = (nodeVal + (1 << i)) % (1 << m)
        # print(tgt)
        cand = binarySearch(nodes, tgt)
        finger_table.append(cand)
    return finger_table

def binarySearch(li, tgt):
    l = 0
    r = len(li)-1
    while l + 1 < r:
        mi = l + (r - l)//2
        if li[mi] < tgt:
            l = mi + 1
        else:
            r = mi
    if li[l] >= tgt:
        return li[l]
    if li[r] >= tgt:
        return li[r]
    return li[0]

m = 8
# nodes = [1, 12, 123, 234, 345, 456, 501]
# nodes = [16,32,45,80,96,112]
nodes = [32,45,99, 132,199, 234]
# nodes = [32,99, 132,199, 234]
for i in range(len(nodes)):
    print(nodes[i], get_finger_table(nodes, m, i))

info = dict({'global':[None]})


def create(namespace, parent):
    info.update({namespace:[parent]})


def add(namespace, var):
    info[namespace].append(var)


def get(namespace, var):
    while namespace is not None and var not in info[namespace][1:]:
        namespace = info[namespace][0]
    print(namespace)


operations = {'create': create, 'add': add, 'get': get}
for i in range(int(input())):
    inp = input().split()
    operations[inp[0]](inp[1], inp[2])
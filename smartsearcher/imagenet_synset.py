import sys

__initialized = False
__relationships = {}
__labels = {}


def __init():
    with open('data/wordnet.is_a.txt') as f:
        for line in f:
            v, k = line.strip().split()
            __relationships[k] = v

    with open('data/words.txt') as f:
        for line in f:
            k, v = line.strip().split('\t')
            __labels[k] = v.split(',')[0]

    __initialized = True


def __tree(wid, existing_labels=[]):
    existing_labels.append(__labels[wid])

    parent = __relationships.get(wid)

    if parent:
        __tree(parent, existing_labels)

    return existing_labels


def tree(wid, existing_labels=[]):
    if not __initialized:
        __init()

    labels = []
    __tree(wid, labels)

    return labels


if __name__ == "__main__":
    print(tree(sys.argv[1]))

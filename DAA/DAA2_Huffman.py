class node:
    def __init__(self,char,freq,left=None,right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.huff = ' '

def prinnt(node, val=''):
        newval = val + str(node.huff)

        if node.left:
            prinnt(node.left, newval)
        if node.right:
            prinnt(node.right, newval)

        if len(node.char)==1:
            print(f"{node.char}==>{newval}")

if __name__=='__main__':
        chars = ['a','b','c','d','e','f']
        freqs = [5,9,12,13,16,45]
        nodes = []

        for i in range(len(chars)):
            nodes.append(node(chars[i],freqs[i]))

        while len(nodes)>1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            left = nodes [0]
            left.huff = 0
            right = nodes[1]
            right.huff = 1
            newnode = node(left.char+right.char, left.freq+right.freq, left, right)
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newnode)

        prinnt(nodes[0])
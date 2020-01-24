def permuteRecursive(d, prefix, target):
    if target == 0:
        print(prefix)
        return
    for i in range(len(d)):
        permuteRecursive(d, prefix+d[i],target-1)
def permute(d, target):
    permuteRecursive(d, "", target)
def main():
    # permute(['a', 'b', 'c'], 3)
    # permute(['a', 'b'], 2)
    permute(['a', 'b'], 3)

main()
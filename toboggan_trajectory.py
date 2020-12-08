
slopes = [ [1, 1], [3, 1], [5, 1], [7,1], [1, 2] ]

positions = [0] * len(slopes)
num_trees = [0] * len(slopes)

with open('toboggan_trajectory_input.txt', mode='r') as f:
    line_number = 0
    for line in f.readlines():
        for si in range(len(slopes)):
            slope = slopes[si]
            if line_number % slope[1] == 0:
                position = positions[si]
                tile = line[position]
                if tile == '#':
                    num_trees[si] += 1
                positions[si] = (position + slope[0]) % (len(line) - 1)
        line_number += 1

print(num_trees)

product = 1
for tree_count in num_trees:
    product *= tree_count
print(product)

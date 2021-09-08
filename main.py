import os

path = input("Path to check: ")
tree = {}
tree_depth = 5
tree_depth_input = input("(Optional) Output depth: ")
if tree_depth_input != "":
    tree_depth = int(tree_depth_input)

min_value = 0
min_value_input = input("(Optional) Minimal value [Mb]: ")
if min_value_input != "":
    min_value = int(min_value_input)


def truncate_by_base_path(subpath):
    return subpath.replace(path, "")


def add_to_nodes(nodes_list, value):
    for node in nodes_list:
        tree.setdefault(node, 0)
        tree[node] += value


def get_nodes_list(subpath):
    nodes_list = []
    folder_list = subpath.split("\\")

    for i in range(len(folder_list)):
        if i < tree_depth:
            nodes_list.append("\\".join(folder_list[0:i+1]))
        else:
            break
    return nodes_list


for (root, dirs, files) in os.walk(path):
    nodes_list = get_nodes_list(truncate_by_base_path(root))
    for file in files:
        add_to_nodes(nodes_list, os.stat(root+"\\"+file).st_size/1000_000)

for key in tree:
    value = tree[key]
    if value >= min_value:
        print(str(key) + "  " + str(value//1) + " Mb")

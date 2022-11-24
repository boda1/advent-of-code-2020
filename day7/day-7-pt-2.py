parent_bag_colours = ['shiny gold']
all_child_bags = {'shiny gold': 1}


def find_parent_colours(current_bag):
    with open('./input.txt') as f:
        for line in f.readlines():
            primary_bag = line.split(' bags contain ')[0]
            bags_to_add = []
            if current_bag == primary_bag:
                bags_to_add = line.split(' bags contain ')[0].split(',')
                all_child_bags + {bag: bag.split(' ')[0] for bag in bags_to_add}


for bag_colour in parent_bag_colours:
    find_parent_colours(bag_colour)


print("All bags that can contain shiny gold: ", parent_bag_colours)
parent_bag_colours.remove('shiny gold')
print("Number of bags that can contain shiny gold: ", len(parent_bag_colours))

"""

Begin with dictionary containing first bag 'shiny gold'
Find the line beginning w shiny gold
Append all bag colours and values in that line to the dictionary

"""
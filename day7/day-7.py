parent_bag_colours = ['shiny gold']


def find_parent_colours(current_bag):
    with open('./input.txt') as f:
        for line in f.readlines():
            primary_bag = line.split(' bags contain ')[0]
            if current_bag in line and current_bag != primary_bag and primary_bag not in parent_bag_colours:
                parent_bag_colours.append(primary_bag)


for bag_colour in parent_bag_colours:
    find_parent_colours(bag_colour)


print("All bags that can contain shiny gold: ", parent_bag_colours)
parent_bag_colours.remove('shiny gold')
print("Number of bags that can contain shiny gold: ", len(parent_bag_colours))


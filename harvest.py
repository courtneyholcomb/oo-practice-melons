############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []



    def add_pairing(self, *new_pairings):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(new_pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types(melon_file):
    """Returns a list of current melon types."""

    all_melon_types = []

    with open(melon_file) as melon_data:
        indiv_melons = melon_data.read().split('\n|\n')

        melons_ingested = []

        for indiv_melon in indiv_melons:

            melon_features = indiv_melon.split('\n')
            melons_ingested.append(melon_features)


        for melon_type in melons_ingested:
            code = melon_type[1][16:]
            first_harvest = melon_type[2][-4:]
            color = melon_type[3][7:]
            name = melon_type[0][6:]


            if melon_type[5] == 'Has seeds':
                is_seedless = True
            else: 
                is_seedless = False

            is_bestseller = "Bestseller" in melon_type

            melon_object = MelonType(code, first_harvest, color, is_seedless,
                is_bestseller, name)

            pairs_with = melon_type[4][16:].split(' and ')

            for pair in pairs_with:
                melon_object.add_pairing(pair)

            all_melon_types.append(melon_object)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for loc_melon in melon_types:
        print(loc_melon.name, "pairs with")
        for pairing in loc_melon.pairings:
            print("-", pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""    
    
    return {melon_type.code:melon_type for melon_type in melon_types}


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    # create initial setup fxn
    def __init__(self, melon, type_code, shape_rat, 
                 color_rat, origin, worker):
        self.melon = melon
        self.type_code = type_code
        self.shape_rat = shape_rat
        self.color_rat = color_rat
        self.origin = origin
        self.worker = worker
    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def is_sellable():
        """Returns True for False based on object's ratings and origin."""

        # if shape and color <= 5, return False
        # if origin field 3, return False
        if shape_rat <=5 or color_rat <=5 or origin == 'Field 3':
            return False

        return True


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 





instantiated_melon_types = make_melon_types("melon_data.txt")

# pairing_info =  print_pairing_info(instantiated_melon_types)

ref_codes = make_melon_type_lookup(instantiated_melon_types)
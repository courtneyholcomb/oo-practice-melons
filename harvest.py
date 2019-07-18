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
        indiv_melons = melon_data.read().split('|')

        melons_ingested = []

        for indiv_melon in indiv_melons:

            melon_features = indiv_melons.split('\n')
            melons_ingested.append(melon_features)

        for melon_type in melons_ingested:
            code = melons_ingested[1][17:]
            first_harvest = melons_ingested[2][-4:]
            color = melons_ingested[3][7:]
            name = melons_ingested[0][6:]

            if melons_ingested[5] == 'Has seeds':
                is_seedless = True
            else: 
                is_seedless = False

            if melons_ingested[6]:
                is_bestseller = True
            else: 
                is_bestseller = False

            melon_object = MelonType(code, first_harvest, color, is_seedless,
                is_bestseller, name)

            melon_object.add_pairing(melons_ingested[4][16:].split(' and '))

            all_melon_types.append(melon_object)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 




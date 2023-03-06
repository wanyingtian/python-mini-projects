'''
You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. 
The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

You will create 3 classes and access their methods, and use them to build a new business
'''
## Part 1: Create Menu Class
class Menu():
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    def __repr__(self):
        self.representative_string = f"The {self.name} menu is available from {self.start_time}:00 to {self.end_time}:00"
        return self.representative_string
    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            bill += self.items.get(item, 0)
        return bill
            
# create 4 menus using Menu Class 
brunch = Menu("Brunch", {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    }, 11, 16 
    )

early_bird = Menu("Early-bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18
)

dinner = Menu("Dinner",{
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

#test out string rep in Menu class
print("- Welcome! Take a look at the brunch menu using string representations")
print(brunch)
#test out calculate_bill method in menu Class
print("- Calculate some bills:")
print(brunch.calculate_bill(['pancakes','home fries','coffee']))
print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

## Part 2: Creating Franchise class
class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        self.representative_string = f"The address of the franchise restaurant is {self.address}"
        return self.representative_string
    def available_menus(self, time):
        avail_menus = []
        for menu in self.menus:
            if (time >= menu.start_time) and (time <= menu.end_time):
                avail_menus.append(menu)
        return avail_menus
        

#create 2 franchise restaurant with all 4 menus
flagship_store = Franchise("1232 West End Road",[brunch, early_bird, dinner, kids])      
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

#test .available_menus() method
print("- What menus are available at 12?")
print(flagship_store.available_menus(12))
print("- What menus are available at 17?")
print(flagship_store.available_menus(17))

## Part 3:  Create Business Class
class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
    def __repr__(self):
        self.representative_string = f"The business {self.name} has {len(self.franchises)} franchise(s)."
        return self.representative_string
    def franchise_addresses(self):
        addresses = []
        for franchise in self.franchises:
            addresses.append(franchise.address)
        return addresses
            
#create first business
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
#create new business with new menu
#first, create arepas menu
arepas_menu = Menu("Arepas",{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)
#second create arepas franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
#third create arepas business
arepas_business = Business("Take a’ Arepa", [arepas_place])

#test business class
print("- Take a look at business 1")
print(basta_fazoolin)
print("- Take a look at business 2")
print(arepas_business)
#test arepas franchise and menu class
print("- Take a look at arepas franchise")
print(arepas_place)
print("- What menu is available at 15:00?")
print(arepas_place.available_menus(15))
print("- How much is 2 jamon arepas?")
print(arepas_menu.calculate_bill(['jamon arepa','jamon arepa']))

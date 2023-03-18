class Aisle:
  counter = 0

  def __repr__(self):
    return self.aisle_description(self.aisle)

  def __init__(self, aisle): 
    self.aisle = aisle
    Aisle.counter += 1
    if Aisle.counter == 13: 
      print(f'\nStore is open for business!\n')

  def aisle_description(self, aisle):
    if aisle == 'front': return f'front of the store, near the registers, restroom and the entrance/exit'
    elif aisle == 'middle': return f'center aisle, the aisle that divides the front and back of the store'
    elif aisle == 'back': return f'back of the store, the meat and cheese aisle'
    elif aisle == 1: return f'produce aisle'
    elif aisle == 2: return f'cereal aisle'
    elif aisle == 3: return f'SB (Specialty Buy) aisle'
    elif aisle == 4: return f'SB Food (Specialty Buy Food) aisle'
    elif aisle == 5: return f'wine and freezer aisle'
    elif aisle == 6: return f'bread and snack aisle'
    elif aisle == 7: return f'juice and can aisle'
    elif aisle == 8: return f'toiletries, cleaning, and paper aisle'
    elif aisle == 9: return f'baking and dinner aisle'
    elif aisle == 10: return f'water, tea/coffee, and cooler aisle'

  def choices(self, aisle):
    if aisle == 'front': 
      print(f'\n[$] for checkout\n[1] to enter produce aisle\n[2] to enter cereal aisle\n[3] to enter SB aisle\n[4] to enter SB food aisle\n[5] to enter wine/freezer aisle\n[remove] to remove an item from your cart\n')
      loc = input(f'Where to?: ')
      return loc
    elif aisle == 'middle': 
      print(f'\n[1] to enter produce aisle\n[2] to enter cereal aisle\n[3] to enter SB aisle\n[4] to enter SB food aisle\n[5] to enter wine/freezer aisle\n[6] to enter bread/snack aisle\n[7] to enter juice/can aisle\n[8] to enter cleaning/paper aisle\n[9] to enter baking/dinner aisle\n[10] to enter drinks/cooler aisle\n[remove] to remove an item from your cart\n')
      loc = input(f'Where to?: ')
      return loc
    elif aisle == 'back': 
      print(f'\n[0] to shop this aisle\n[6] to enter bread/snack aisle\n[7] to enter juice/can aisle\n[8] to enter cleaning/paper aisle\n[9] to enter baking/dinner aisle\n[10] to enter drinks/cooler aisle\n[remove] to remove an item from your cart\n')
      loc = input(f'Where to?: ')
      return loc
    elif aisle == 1 or aisle == 2 or aisle == 3 or aisle == 4 or aisle == 5: 
      print(f'\n[0] to shop this aisle\n[front] to go to the front of the store\n[middle] to go to the middle aisle\n[remove] to remove an item from your cart\n')
      loc = input(f'Where to?: ')
      return loc
    elif aisle == 6 or aisle == 7 or aisle == 8 or aisle == 9 or aisle == 10:
      print(f'\n[0] to shop this aisle\n[back] to go to the back of the store, the meat/cheese aisle\n[middle] to go to the middle aisle\n[remove] to remove an item from your cart\n')
      loc = input(f'Where to?: ')
      return loc
    else:
      return

class Cart:
  cart_items = []
  cart_prices = []

  def __repr__(self):
    if len(self.cart_items) == 0: return f'{self.shopper}\'s cart is empty, you should probably do some shopping.'
    elif len(self.cart_items) == 1: return f'{self.shopper} has just 1 item in the cart, lets look around some more.'
    elif len(self.cart_items) >= 2:
      return f'{self.shopper}\'s cart has {len(self.cart_items)} items in it, let\'s not be frugal now, you know you need more than that.'
    elif len(self.cart_items) >= 10:
      return f'{self.shopper}\'s cart has {len(self.cart_items)} items in it, is this enough to feed your family?'
    elif len(self.cart_items) >= 25: 
      return f'{self.shopper}\'s cart has {len(self.cart_items)} items in it, that\'s more like it!'
    elif len(self.cart_items) >= 50:
      return f'{len(self.cart_items)} items in the cart...I think that\'s enough now {self.shopper}, you have a budget.'
    elif len(self.cart_items) >= 100:
      return f'{len(self.cart_items)} items in the cart!?!?  {self.shopper}, do you program for a living?!?!?'

  def __init__(self, shopper):
    self.shopper = shopper
    print(f'{shopper} is ready to shop!\n')

  def add_to_cart(self, item, loc):
    self.cart_items.append(item)
    index = Shopper.position_to_names(Shopper, loc).index(item)
    self.cart_prices.append(Shopper.position_to_prices(Shopper, loc)[index])
    print(f'\n{item} added to the cart')
    print(f'${Shopper.position_to_prices(Shopper, loc)[index]} added to the cart total')

  def remove_from_cart(self, pos):
    print(f'Cart Contents...\n')
    if self.cart_items == []: 
      print(f'Your cart is empty, you can\'t remove anything from it.\n')
      print(f'You are in the {Aisle.aisle_description(Aisle, pos)}')
      return
    cart_contents = [[cart_item, cart_price] for cart_item, cart_price in zip(self.cart_items, self.cart_prices)]
    for content in cart_contents:
      print(f'{content[0]}: ${content[1]}')
    print(f'\nEnter \'done\' to go back to shopping')
    item = input(f'What would you like to remove from the cart?\n')
    if not item.title() in self.cart_items and not item.lower() == 'done':
      print(f'That item isn\'t in the cart.')
      self.remove_from_cart(self, pos)
    elif item.lower() == 'done':
      print('\n')
      print(Aisle.aisle_description(Aisle, pos))
      return
    price_index = self.cart_items.index(item.title())
    price_to_remove = self.cart_prices[price_index]
    self.cart_items.remove(item.title())
    self.cart_prices.pop(price_index)
    print(f'\n{item.title()} removed from the cart')
    print(f'${price_to_remove} removed from the cart total\n')  
    print(Aisle.aisle_description(Aisle, pos))

  def get_reciept(self, name):
    reciept_items = [[cart_item, cart_price] for cart_item, cart_price in zip(self.cart_items, self.cart_prices)]
    for rec_item in reciept_items:
      print(f'{rec_item[0]}:     ${rec_item[1]}')
    subtotal = round(sum(self.cart_prices), 2)
    tax = round(subtotal * 0.07, 2)
    print(f'\nSubtotal:      ${subtotal}')
    print(f'Sales Tax:     ${tax}')
    print(f'Total:         ${round(subtotal + tax, 2)}')
    print(f'\n{name}, you spent ${round(subtotal + tax, 2)} on {len(self.cart_items)} item(s).')
    return

class Shopper:
  
  def __repr__(self):
    intro = f'You are in the '
    if self.position == 'front': return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 'middle': return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 'back': return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 1: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 2: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 3: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 4: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 5: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 6: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 7: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 8: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 9: return intro + Aisle.aisle_description(self, self.position)
    elif self.position == 10: return intro + Aisle.aisle_description(self, self.position)
    
  def __init__(self, name, sex):
    self.name = name 
    self.position = 'front'
    if sex == 'male': self.sex = 'sir'
    else: self.sex = 'ma\'am'
    self.cart = Cart(name)
    print(f'{self.name} grabs a cart and enters the store...\n')
    print(self)

  def get_position(self):
    return self.position

  def position_to_items(self, position):
    if position == 'back': return meat_cheese
    elif position == 1: return produce
    elif position == 2: return cereal
    elif position == 3: return sb
    elif position == 4: return sb_food
    elif position == 5: return wine_freezer
    elif position == 6: return bread_snack
    elif position == 7: return juice_can
    elif position == 8: return cleaning_paper
    elif position == 9: return baking_dinner
    elif position == 10: return drinks_cooler

  def position_to_names(self, position):
    if position == 'back': return meat_cheese_names
    elif position == 1: return produce_names
    elif position == 2: return cereal_names
    elif position == 3: return sb_names
    elif position == 4: return sb_food_names
    elif position == 5: return wine_freezer_names
    elif position == 6: return bread_snack_names
    elif position == 7: return juice_can_names
    elif position == 8: return cleaning_paper_names
    elif position == 9: return baking_dinner_names
    elif position == 10: return drinks_cooler_names

  def position_to_prices(self, position):
    if position == 'back': return meat_cheese_prices
    elif position == 1: return produce_prices
    elif position == 2: return cereal_prices
    elif position == 3: return sb_prices
    elif position == 4: return sb_food_prices
    elif position == 5: return wine_freezer_prices
    elif position == 6: return bread_snack_prices
    elif position == 7: return juice_can_prices
    elif position == 8: return cleaning_paper_prices
    elif position == 9: return baking_dinner_prices
    elif position == 10: return drinks_cooler_prices
  
  def move(self, loc):
    if str(loc) == '$': return self.checkout()
    elif str(loc.lower()) == 'remove': return Cart.remove_from_cart(Cart, self.position)
    elif loc == '0': return self.shop(self.position)
    elif loc == 'front' or loc == 'middle' or loc == 'back':
      self.position = loc
      print(f'\n{self.name} walked to the {loc} of the store.\n')
      print(self)
      return 
      # Aisle.choices(self.position)
    elif loc == '1' or loc == '2' or loc == '3' or loc == '4' or loc == '5' or loc == '6' or loc == '7' or loc == '8' or loc == '9' or loc == '10':
      self.position = int(loc)
      print(f'\n{self.name} walked to aisle {loc}.\n')
      print(self)
      return 
      # Aisle.choices(self, self.position)
    else:
      print(f'\nThats an invalid input, try again.\n')
      print(self)
      return

  def shop(self, position):
    if position == 'front' or position == 'middle': 
      print(f'\nCan\'t shop this aisle.\n')
      print(self)
      return 
    else:
      items_for_sale = self.position_to_items(self.position)
      list_of_items = self.position_to_names(self.position)
      print(items_for_sale)
      print(f'Enter \'done\' when you are finshed shopping or...')
      buy = input(f'Enter the name of what you would to buy then hit enter (one item at a time)\n')
      if buy.lower() == 'done':
        print('\n')
        print(self)
        return 
        # Aisle.choices(self.position)
      else:
        if buy.title() in list_of_items:
          Cart.add_to_cart(Cart, buy.title(), self.position)
          return self.shop(self.position)
        else:
          print('I don\'t think we sell that item, sorry.')
          return self.shop(self.position)

  def checkout(self):
    choice = input(f'\nCashier: Are you ready to checkout?\n[Yes] or [No]\n')
    if choice == 'no' or choice == 'NO' or choice == 'No':
      print(f'\nThat\'s fine, I\'ll be here when you\'re ready to checkout!\n')
      print(self)
      return 
      # Aisle.choices(self.position)
    elif choice == 'yes' or choice == 'YES' or choice == 'Yes':
      print(f'\nCashier: Hi, I hope you found everything you were looking for!\n')
      count = len(Cart.cart_items)
      while count > 0:
        if count == 1:
          print('BEEP!\n')
        else: print('beep...')
        count -= 1
      tax = sum(Cart.cart_prices) * 0.07
      print(f'Cashier: Alrighty, your total came out to ${round((sum(Cart.cart_prices) + tax), 2)} dollars.\n')
      cash_card = input(f'Cashier: Cash or card today?\n[1] for Cash\n[2] for card\n')
      if cash_card == '1':
        print(f'{self.name} looks in wallet to see no cash...\n')
        print(f'{self.name} pays with card instead\n')
      for x in range(10):
        print(f'paying...')
      print(f'DING! Payment Complete\n')
      print(f'Reciept printing...\n')
      print(f'Cashier: Here\'s that reciept, have a good day {self.sex}\n')
      print(f'Thanks for shopping {self.name}!\nMake sure to check over your reciept for any discrepencies\n')
      print(f'SHOPPING EXPERIENCE FINISHED\n')
      print(f'{self.name} looks at reciept...\n')
      print(Cart.get_reciept(Cart, self.name))
      finished = f'\nGoodbye!'
      return finished
    else:
      print(f'Cashier: I\'m sorry, what was that?\n')
      return self.checkout()

class Item:

  def __repr__(self):
    print('\n')
    for item in self.items:
      print(f'{item[0]}: ${item[1]}')
    return f'\nItems for sale in the {self.title} aisle ({len(self.items)} items)\n'

  def __init__(self, title, names, prices):
    self.title = title
    self.items = [[name, price] for name, price in zip(names, prices)]


#-----------------------------------------------------------------------------------------------------------------------------------#


# Create the lists of items to turn into Item objects
produce_names = ['Celery', 'Red Grapes (2 Lb)', 'Green Grapes (2 Lb)', 'Envy Apples (3 Lb)', 'Honeycrisp Apples (3 Lb)', 'Cilantro', 'Parsley', 'Carrots (2 Lb)', 'Broccoli', 'Spinach', 'Lettuce', 'Cabbage', 'Strawberries', 'Blueberries', 'Blackberries', 'Raspberries', 'Shredded Lettuce', 'Italian Salad', 'Spring Mix', 'Garden Salad', 'Romaine Lettuce', 'Red Onions', 'Sweet Onions', 'Yellow Onions', 'White Onions', 'Beefsteak Tomatoes', 'Tomatoes On The Vine', 'Grape Tomatoes', 'Zucchini', 'Yellow Squash', 'Butternut Squash', 'Acorn Squash', 'Spaghetti Squash', 'Green Peppers', 'Mixed Bell Peppers', 'Jalapenos', 'Garlic', 'Ginger Root']
produce_prices = [1.99, 1.99, 2.49, 2.79, 2.69, 1.69, 1.89, 1.49, 1.37, 1.99, 1.29, 1.19, 2.99, 2.99, 2.79, 2.69, 2.29, 2.19, 2.29, 2.09, 2.99, 2.49, 1.79, 1.99, 2.69, 1.79, 1.89, 1.99, 2.99, 2.99, 3.99, 3.99, 3.99, 1.59, 1.89, 1.19, 0.89, 0.89]

cereal_names = ['Fruity Loops', 'Frosted Mini Biscuits', 'Cocoa Puff Balls', 'Captain Crunchy Berries', 'Protein Pancakes', 'Granola Bars']
cereal_prices = [2.49, 1.99, 2.69, 2.99, 2.89, 2.89, 1.99]

sb_names = ['Ladies Cute Shirt', 'Mens Puffer Jacket', 'Cast Iron Cutting Board', 'Gazebo', 'A/C Unit', 'Swimming Pool', 'Glow-In-The-Dark Markers']
sb_prices = [3.99, 6.99, 12.99, 299.99, 149.99, 89.99, 0.99]

sb_food_names = ['Flamin Hot Cheedos Family Size', 'Dill Pickle Chips', 'Hot Wok Ramen', 'Extra Appley Apple Juice', 'Vegan Protein Powder', 'Cranberry Pineapple Walnut Sparkling Water Cans (12 pack)', 'Yakisoobi Beef', 'Yakisoobi Chicken']
sb_food_prices = [4.99, 2.99, 6.99, 3.19, 27.99, 5.98, 0.99, 0.99]

wine_freezer_names = ['(Wine) Red Blend Box Wine', '(Wine) Chateau Elan Sauvignon Blanc', '(Wine) Waking Owl Sangria', '(Wine) Waking Owl Cabernet', '(Wine) Waking Owl Merlot', '(Wine) Waking Owl Pinot Grigio', '(Wine) Waking Owl Pinot Noir', '(Freezer) White Sandcastles', '(Freezer) Ice Cream Sandwiches', '(Freezer) Chocolate Ice Cream', '(Freezer) Vanilla Ice Cream', '(Freezer) Frozen Mochi', '(Freezer) Turkey Sausage', '(Freezer) Crispy Chicken Tenders', '(Freezer) Broccoli Florets', '(Freezer) Shrimp Scampi', '(Freezer) Fettucine Alfredo', '(Freezer) Vegan Patties', '(Freezer) Lobster Mac N Cheese', '(Freezer) Sea Scallops', '(Freezer) Mama Cuzzi Pepperoni Rising Crust', '(Freezer) Mama Cuzzi Supreme Rising Crust', '(Freezer) Mama Cuzzi Cheese Rising Crust']
wine_freezer_prices = [12.99, 9.99, 9.99, 3.99, 3.99, 3.99, 3.99, 10.99, 2.99, 2.19, 2.09, 3.79, 3.99, 4.49, 1.19, 6.99, 6.89, 3.89, 5.69, 12.99, 3.29, 3.29, 3.29]

bread_snack_names = ['(Bread) Honey Wheat', '(Bread) White Sandwich', '(Bread) Bens Killa Bread', '(Snack) Honey Bunn', '(Snack) Chill Ranch Triangle Chips', '(Snack) Slimmy Jims', '(Snack) Takitos']
bread_snack_prices = [0.49, 0.69, 4.99, 2.99, 1.49, 1.89, 2.19]

juice_can_names = ['(Juice) Grape Juice', '(Juice) Pomegranate Juice', '(Juice) Apple Juice', '(Can) Green Beans', '(Can) Yellow Corn', '(Can) Cream Corn', '(Can) Black Beans']
juice_can_prices = [2.89, 3.09, 2.39, 0.84, 0.69, 0.79, 0.72]

cleaning_paper_names = ['Paper Towel (2 Pack)', 'Paper Towel (6 Pack)', 'Toilet Paper (24 Pack)', 'Toilet Cleaner', 'Deoderant', 'Toothbrush', 'Laundry Detergent', 'Tissues']
cleaning_paper_prices = [3.99, 5.49, 5.99, 4.29, 1.99, 0.99, 7.99, 1.09]

baking_dinner_names = ['Orzo Pasta', 'Spaghetti Noodles', 'Mac N Cheese', 'Traditional Pasta Sauce', 'Vodka Sauce', 'Muffin Mix', 'Canola Oil', 'Spray Oil', 'Brownie Mix', 'Chicken Ramon', 'Beef Ramon']
baking_dinner_prices = [2.29, 1.99, 1.49, 1.59, 2.49, 2.69, 1.89, 1.89, 1.99, 2.89, 2.89]

drinks_cooler_names = ['(Drinks) Purified Water (24 Pack)', '(Drinks) Spring Water (24 Pack)', '(Drinks) Herbal Tea', '(Drinks) Dark Roast Ground Coffee', '(Cooler) Eggs', '(Cooler) Orange Juice', '(Cooler) Sweetened Almondmilk', '(Cooler) Unsweetened Almondmilk', '(Cooler) Oatmilk', '(Cooler) Bacon', '(Cooler) Butter', '(Cooler) Cream Cheese']
drinks_cooler_prices = [2.49, 2.79, 2.39, 2.49, 4.79, 2.89, 2.19, 2.19, 2.49, 6.99, 1.37, 1.19]

meat_cheese_names = ['(Meat) Ground Turkey', '(Meat) Boston Butt Roast', '(Meat) Chuck Roast', '(Meat) 80/20 Ground Beef', '(Meat) Chicken Breasts', '(Cheese) Sliced Chedder Cheese', '(Cheese) Sliced Pepper Jack Cheese', '(Cheese) Shredded Chedder Cheese', '(Cheese) Shredded Mozzarella Cheese']
meat_cheese_prices = [3.99, 12.39, 11.49, 4.49, 4.89, 1.99, 1.79, 2.09, 2.39]

# Instantiate Item objects
produce = Item('produce', produce_names, produce_prices)
cereal = Item('cereal', cereal_names, cereal_prices)
sb = Item('specialty buy', sb_names, sb_prices)
sb_food = Item('specialty buy food', sb_food_names, sb_food_prices)
wine_freezer = Item('wine/freezer', wine_freezer_names, wine_freezer_prices)
bread_snack = Item('bread/snack', bread_snack_names, bread_snack_prices)
juice_can = Item('juice/can', juice_can_names, juice_can_prices)
cleaning_paper = Item('cleaning/paper', cleaning_paper_names, cleaning_paper_prices)
baking_dinner = Item('baking/dinner', baking_dinner_names, baking_dinner_prices)
drinks_cooler = Item('drinks/cooler', drinks_cooler_names, drinks_cooler_prices)
meat_cheese = Item('meat/cheese', meat_cheese_names, meat_cheese_prices)

# Instantiate the aisles (The entire store)
front = Aisle('front')
middle = Aisle('middle')
back = Aisle('back')
aisle1 = Aisle(1)
aisle2 = Aisle(2)
aisle3 = Aisle(3)
aisle4 = Aisle(4)
aisle5 = Aisle(5)
aisle6 = Aisle(6)
aisle7 = Aisle(7)
aisle8 = Aisle(8)
aisle9 = Aisle(9)
aisle10 = Aisle(10)

# Instantiate shopper (Cart instanstiates with shopper)
ben = Shopper('Ben', 'male')

shopping = True
while shopping:
  loc = Aisle.choices(ben, ben.position)
  finished = Shopper.move(ben, loc)
  if finished:
    print(finished)
    break
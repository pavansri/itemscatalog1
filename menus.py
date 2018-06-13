from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, FoodItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Pavan", email="pavansri97@gmail.com")
session.add(User1)
session.commit()

# Menu for Food court
restaurant1 = Restaurant(name="Food court", user_id="1")

session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Suprabhath Multi cuisine")

session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Chandrika")

session.add(restaurant3)
session.commit()

menuItem1 = FoodItem(name="Masala Dosa",
                     description="Crepe made from rice"
                     "batter and black lentils.",
                     price="$2.99", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem2 = FoodItem(name="Sambar Idly",
                     description=" Rice cake with"
                     "lentil-based vegetable stew.",
                     price="$7.50",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = FoodItem(name="Pongal",
                     description="South indian porridge"
                     "made with rice and yellow moong lentils.",
                     price="$5.50", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Menu for Suprabhath Multi cuisine.

menuItem1 = FoodItem(name="Veg Biryani",
                     description="Rice dish layered with vegetables.",
                     price="$7.99", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = FoodItem(name="Avakai Biryani",
                     description="Rice dish"
                     "layered with vegetables and mango pickle.",
                     price="$25",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = FoodItem(name="Kabab Biryani",
                     description="Rice dish with Chicken kababs and boneless curry."
                     "made with chicken.",
                     price="$17", restaurant=restaurant2)

session.add(menuItem3)
session.commit()


menuItem1 = FoodItem(name="Milkshake",
                     description="skimmed creamy milk",
                     price="$2.0", restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = FoodItem(name="Choclate Milkshake",
                     description="Choclate mixed with skimmed creamy milk",
                     price="$4.0", restaurant=restaurant3)

session.add(menuItem2)
session.commit()

print "Added Food items!"

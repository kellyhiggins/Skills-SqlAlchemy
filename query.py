"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter(or_(Brand.discontinued != None, Brand.founded < 1950).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)
# format with \n newlines or \t tabs

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model.name,
                              Model.brand_name,
                              Brand.headquarters).join(Brand)
                              .filter(Model.year == year)
                              .all()

    for name, brand_name, headquarters in models:
        print "Model: %s Brand: %s Headquarters: %s" %(name, brand_name, headquarters)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     cars = db.session.query(Model.brand_name, Model.name).group_by('brand_name', 'name').all()

    for car in cars:
        print car.brand_name, car.name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# The return of that query is an object, of the SqlAlchemy class Brand. The value
# it returns will be the location of that object in memory.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table is an intermediary between two tables that would otherwise
# have a 'many-to-many' relationship. It will have primary keys for the tables
# that it is connecting, represented as foreign keys.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Takes in any string as a parameter, and returns a list of objects that are
    brands whose name contains or is equal to the input string"""

    brands = Brand.query.filter((Brand.name == mystr) | (Brand.name.like(%mystr%)).all()
# I'm not sure if this is the right way to search this. Would it make sense to do string 
# substitution? 
#   brands = Brand.query.filter((Brand.name == mystr) | (Brand.name.like('%%s%) %(mystr)).all()

    return brands

def get_models_between(start_year, end_year):
    """Takes in a start_year and end_year as integers, and returns a list of objects
    that are models with years that fall between the start year and end year.""" 
    
    models = Model.query.filter( (Model.year >= start_year) & (Model.year < end_year).all()

    return models

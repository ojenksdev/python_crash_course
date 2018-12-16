# Writing a T-Shirt making function


def make_shirt(size='lg', text='i love python'):
    """Takes a T-shirt order including size and wording"""
    print("Your T-shirt is a size " + size.upper() + " and says " +
          text.title())


make_shirt()
make_shirt(size='md')
make_shirt(text='when moon?')

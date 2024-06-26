'''
You have been given the class Band. Extend the class such that it will produce specific output when using the print and repr.
Expected Output
Initialize an object of the Band class as follows:
dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])
Command	Output
print(dead)	The Grateful Dead is a rock’n roll band.
print(repr(dead))	Band(The Grateful Dead, rock’n roll, ['Jerry’, 'Bob’, 'Mickey’, 'Bill’, 'Phil’, ‘Pigpen’])
'''

#Code:
class Band:
  def __init__(self, name, genre, members):
    self.name = name
    self.genre = genre
    self.members = members
    
  def __str__(self):
    return f'{self.name} is a {self.genre} band.'
  
  def __repr__(self):
    return f'Band({self.name}, {self.genre}, {self.members})'
  
dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])
print(dead)
print(repr(dead))
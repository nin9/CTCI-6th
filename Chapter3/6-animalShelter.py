from collections import deque

class Animal:
  def __init__(self, name: str) -> None:
    self.name = name
    self.order = 0

  def isOlder(self, animel: 'Animal') -> bool:
    return self.order < animel.order

class Dog(Animal):
  pass

class Cat(Animal):
  pass


class AnimalQueue:
  def __init__(self) -> None:
    self.dogs = deque()
    self.cats = deque()
    self.order = 0

  def enqueue(self, animel: 'Animal') -> None:
    animel.order = self.order
    self.order += 1

    if isinstance(animel, Dog):
      self.dogs.append(animel)
    else:
      self.cats.append(animel)

  def dequeueAny(self) -> 'Animal':
    if len(self.dogs) == 0:
      return self.dequeueCat()
    elif len(self.cats) == 0:
      return self.dequeueDog()
    dog = self.dogs[0]
    cat = self.cats[0]
    if cat.isOlder(dog):
      return self.dequeueCat()
    return self.dequeueDog()

  def dequeueCat(self) -> 'Animal':
    return self.cats.popleft()

  def dequeueDog(self) -> 'Animal':
    return self.dogs.popleft()



queue = AnimalQueue()

queue.enqueue(Cat('cat1'))
queue.enqueue(Cat('cat2'))
queue.enqueue(Dog('dog1'))
queue.enqueue(Dog('dog2'))

print(queue.dequeueAny().name)
print(queue.dequeueAny().name)
print(queue.dequeueAny().name)
def outer_function():
  counter = 0
    
  def inner_function():
    nonlocal counter  # Declare counter as nonlocal
    counter += 1
    return counter

  return inner_function

increment = outer_function()
print(increment())  # Output: 1
print(increment())  # Output: 2 (modified counter in outer function)

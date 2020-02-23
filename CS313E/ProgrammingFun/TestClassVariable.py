# Aidan O'Keeffe

# Tests if attributes can be set recursively whatever no one will read this

# Arbitrary object
class TestObject(object):
  # Intersting. A class with no attributes doesn't need a constructor!
  def __str__(self):
    return "<class 'TestObject'>"

  # Defines abritrary attribute attb, calls test_helper()
  def test(self, attb = 0):
    self.attb = attb
    return(self.test_helper(self.attb))

  def test_helper(self, num = 0):
    if num == 0:
      return self.attb
    else:
      return 1 + self.test_helper(num - 1)













def main():
  test = TestObject()
  print(test)
  print()

  lo = int(input("Enter lower: "))
  hi = int(input("Enter upper: "))
  print()
  for i in range(lo, hi + 1):
    print("i = " + str(i))
    print("test.attb = " + str(test.test(i)))
  

main()
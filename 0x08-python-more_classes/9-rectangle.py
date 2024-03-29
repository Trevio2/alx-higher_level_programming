
#!/usr/bin/python3 
 """This module is for the rectangle class"""


 class Rectangle:
         """Class Rectangle that defines the object"""

         number_of_instances = 0 
          print_symbol = '#'

          def __init__(self, width=0, height=0):
                  """Initialize the object"""
                  self.width = width 
                   self.height = height
                   Rectangle.number_of_instances += 1

               @property 
                def width(self): 
                   """getter method for width""" 
                    return self.__width

                      @width.setter 
                       def width(self, value):
               """setter method for the width attribute"""
                           if type(value) != int:
                raise TypeError("width must be an integer"
                raise ValueError("width must be >= 0")
                        self.__width = value

                    @property 
                     def height(self):
                         """getter method for height"""
                         return self.__height

                     @height.setter 
                   def height(self, value): 
                        """setter method for the height attribute"""
                 if type(value) != int: 
                raise TypeError("height must be an integer")
                        if value < 0: 
                raise ValueError("height must be >= 0") 
                          self.__height = value

                      def area(self): 
                           """returns the rectangle area""" 
                     return self.__width * self.__height

                    def perimeter(self):
                """returns the rectangle perimeter"""
                if self.__width == 0 or self.__height == 0:
                return 0
                return 2 * (self.__width + self.__height)

                    def __str__(self):
                        """prnts the rectacter with a character #"""
                        if self.width == 0 or self.height == 0:
                            return "" 
                         return '\n'.join(str(
                          self.print_symbol) * self.__width for i in range(self.__height))

                     def __repr__(self):
                         """official string representation of the object rectangle"""
                         return "Rectangle({}, {})".format(self.__width, self.__height)

            def __del__(self):
                 """this is the method of deletion"""
                         Rectangle.number_of_instances -= 1 
                          print("Bye rectangle...")

                              @staticmethod 
           def bigger_or_equal(rect_1, rect_2):
              """static method that returns which is bigger"""                  if not isinstance(rect_1, Rectangle):
                  raise TypeError("rect_1 must be an instance of Rectangle")
              if not isinstance(rect_2, Rectangle):
      raise TypeError("rect_2 must be an instance of Rectangle")
              if rect_1.area() >= rect_2.area():
                    return rect_1
                else:
                    return rect_2

                    @classmethod
                    def square(cls, size=0):
                    """class method that return new Rectangle instance"""
                            if type(value) != int:
                        raise TypeError("width must be an integer")

class Objeto:

  """
  :version:
  :author:
  """

  def __init__(self, image):
        self.__image = image
  
  def __str__(self):
      return "image: {0}".format(self.__image)

  def mostrarImagen(self):
    """
     

    @return  :
    @author
    """
    return self.__image




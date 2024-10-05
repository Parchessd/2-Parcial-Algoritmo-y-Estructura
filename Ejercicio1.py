class Code:
   def __init__(self, descripcion, ID, FechaExp, INFO):
      self.decripcion = descripcion
      self.ID = ID
      self.FechaExp = FechaExp
      self.INFO = INFO
      
      
def cambiar_datos(self, descripcion=None, ID=None, FechaExp=None, INFO=None):
   if descripcionis not None:
self.descripcion = descripcion
if ID is not None:
   self.ID = ID  
   if FechaEXP is not None:
      self.FechaExp = FechaExp
if INFO is not None:
   Self.INFO = INFO 


def calcular_expirados(self):
   now = datetime.now().date()
      if self.FechaExp < now:
      raise Exception("El producto ha expirado.")
      


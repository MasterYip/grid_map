from grid_map_python import GridMapBinding
from grid_map_python import SignedDistanceFieldBinding
from .convert import from_msg, to_msg

class GridMap(GridMapBinding):
	def __setitem__(self, layer, val):
		self[layer][:] = val

	def __repr__(self):
		return f'<{self.getLength()[0]:.2f}x{self.getLength()[1]:.2f}x{self.getResolution():.2f} grid on {self.getLayers()} at {self.getPosition()}>'

	@classmethod
	def from_msg(cls, msg):
		return from_msg(msg, cls)

	def to_msg(self):
		return to_msg(self)

class SignedDistanceField(SignedDistanceFieldBinding):
    
	def __repr__(self):
		return f'<{self.size()[0]:.2f}x{self.size()[1]:.2f}x{self.size()[2]:.2f} sdf>'

	def derivative(self, position):
		return self.valueAndDerivative(position)[1]
import io

class RunLength:
	def __init__(self):
		self.width = 800
		self.height = 450
		self.num_frames = 150

	def encode(self, base):
		input_stream = open('/Users/ijohnnyh/Documents/School/Classwork/COMP590/A1VideoFiles/'+base+'/'+base+'.450p.yuv', 'rb')
		output_stream = open('/Users/ijohnnyh/Documents/School/Classwork/COMP590/A1VideoFiles/'+base+'/'+base+'.450p-encoded.dat', 'w+b')

		for frame in range(0, self.num_frames):
				print ('ENCODING FRAME {0}'.format(frame))
				prev_symbol = input_stream.read(1)
				occur = 1
				for pixels in range(1, self.width * self.height):
					curr_symbol = input_stream.read(1)
					if (prev_symbol != curr_symbol):
						output_stream.write(prev_symbol)
						output_stream.write(bytes([occur]))
						output_stream.flush()
						prev_symbol = curr_symbol
						occur = 1
					elif prev_symbol == curr_symbol:
						if (occur == 255):
							output_stream.write(curr_symbol)
							output_stream.write(bytes([occur]))
							output_stream.flush()
							occur = 1
						else:
							occur+=1
		input_stream.close()
		output_stream.close()

	def decode(self, base):
		input_stream = open('/Users/ijohnnyh/Documents/School/Classwork/COMP590/A1VideoFiles/'+base+'/'+base+'.450p-encoded.dat', 'rb')
		output_stream = open('/Users/ijohnnyh/Documents/School/Classwork/COMP590/A1VideoFiles/'+base+'/'+base+'.450p-decoded.dat', 'w+b')
		for frame in range(0, self.num_frames):
			print ('DECODING FRAME {0}'.format(frame))
			for pixels in range(0, self.width*self.height):
				symbol = input_stream.read(1)
				occur = int.from_bytes(input_stream.read(1), byteorder='big')
				for i in range(0, occur):
					output_stream.write(symbol)
				output_stream.flush()

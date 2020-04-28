from fpdf import FPDF
import PyPDF2

class Convert:
	"""
	To conver file between .txt(text files), .pdf(pdf 
	files) and .wav(audio files). The conversion to .wav
	is an idea for making audiobooks
	"""

	def __init__(self):
		self.file = input("Enter complete file path: \n")
		
		self.first_thing()

	def first_thing(self):
		try:
			name = [i for i in self.file.split('\\')]
		except:
			name = [i for i in self.file.split('/')]
		file_name = name[-1]
		try:
			f_t = [i for i in file_name.split('.')]
		except:
			pass
			# to work on adding file extensions
			# another seperate project to be imported
		file_type = f_t[1]
		self.name = f_t[0]

		if file_type == 'txt':
			print("File to be converted to .pdf[0] or .wav[1]")
			command = int(input("Enter digit for file type conversion: \n"))
			if command == 0:
				self.text_to_pdf()
			elif command = 1:
				self.text_to_wav()
			else:
				print("Invalid command!")
				self.first_thing()
		elif file_type == 'pdf':
			print("File to be converted to .txt[0] or .wav[1]")
			command = int(input("Enter digit for file type conversion: \n"))
			if command == 0:
				self.pdf_to_text()
			elif command = 1:
				self.pdf_to_wav()
			else:
				print("Invalid command!")
				self.first_thing()
		elif file_type == 'wav':
			print("File to be converted to .pdf[0] or .txt[1]")
			command = int(input("Enter digit for file type conversion: \n"))
			if command == 0:
				self.wav_to_pdf()
			elif command = 1:
				self.wav_to_text()
			else:
				print("Invalid command!")
				self.first_thing()
		else:
			print("Invalid file type!")
			print("Can only convert between .txt, .pdf & .wav")

	def pdf_to_text(self):
		pass

	def text_to_pdf(self):
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size=12)
		with open(self.file, 'r') as f:
			lines = f.readlines()
		num = 1
		for line in lines:
			pdf.cell(200, 10, txt=line, ln=num, align='C')
			num += 1

		pdf.output(self.name'.pdf')

	def to_wav(self):
		pass



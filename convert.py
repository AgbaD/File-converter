import os
from fpdf import FPDF
import PyPDF2
from gtts import gTTS

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
			print("Invalid File Name1")
			return

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
			print("Cannot convert fromwav :( ")
		else:
			print("Invalid file type!")
			print("Can only convert between .txt, .pdf & .wav")

	# There is an issue here
	def pdf_to_text(self):
		pdf_file = open(self.file, 'rb')
		pdf_reader = PyPDF2.PdfFileReader(pdf_file)
		n = pdf_reader.getNumPages()
		text = ''
		for i in range(n):
			pg = pdf_reader.getPage(x-1)
			text += pg.extractText()

		file_name = '{0}.txt'.forman(self.name)
		path = os.getcwd()
		file_path = os.path.join(path, file_name)
		with open(file_path, 'a') as f:
			f.writelines(text)
		pdf_file.close()

	def pdf_to_wav(self):
		# call pdf_to_text
		# then call text_to_wav
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

		pdf.output('{0}.pdf'.format(self.name))

	def text_to_wav(self):
		with open(self.file) as f:
			txt = f.read()

		audio = gTTS(text=txt, lang='en', slow=Fasle)
		audio.save("{0}.wav".format(self.name))


#!/usr/bin/python
# Author:	@BlankGodd

from fpdf import FPDF
from gtts import gTTS

class Convert:
	"""
	To convert file between .txt(text files) to .pdf(pdf 
	files) and .wav(audio files). The conversion to .wav
	is an idea for making audiobooks
	"""

	def __init__(self):
		self.file = input("Enter complete file path: \n")
		print()
		print("Enter [0] to convert to pdf or [1] to convert to wav")
		print()
		command = int(input("Enter Input: "))
		if command == 0:
			self.name = input("Enter name to save file as: \n:")
			self.text_to_pdf()
		elif command == 1:
			self.name = input("Enter name to save file as: \n:")
			self.text_to_wav()
		else:
			print("Invalid Input!")


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



"""
Translates user input from one language to other specified languages
"""
#importing all necessary libraries
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#using watson language translate instance. You can use your own, read the readme file for further info
URL_LT = 'YOUR_WATSON_TRANSLATOR_URL_KEY'
APIKEY_LT = 'YOUR_WATSON_TRANSLATOR_API_KEY'
VERSION_LT = '2018-05-01' #CHECK FOR THE LATEST DATE IN DOCUMENTATION

#building an autheticator and translation model
authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(URL_LT)
language_translator

lang1 = ["english", "English", "ENGLISH"]
lang2 = ["german", "German", "GERMAN"]
lang3 = ["french", "French", "FRENCH"]
lang4 = ["spanish", "Spanish", "SPANISH"]

def translator():
	user_input1 = input("Enter from which language you want to convert: ")
	user_input2 = input("Enter to which language you want to convert: ")
	your_text = input("enter: ")
	if user_input1 in lang1:
		if user_input2 in lang2:
			englishtogerman(your_text)
		elif user_input2 in lang3:
			englishtofrench(your_text)
		elif user_input2 in lang4:
			englishtospanish(your_text)
		else:
			print("Enter a correct language")
	elif user_input1 in lang2:
		if user_input2 in lang1:
			germantoenglish(your_text)
		elif user_input2 in lang3:
			germantofrench(your_text)
		elif user_input2 in lang4:
			print('Sorry, german to spanish not supported')
		else:
			print("Enter a correct language")
	elif user_input1 in lang3:
		if user_input2 in lang1:
			frenchtoenglish(your_text)
		elif user_input2 in lang2:
			frenchtogerman(your_text)
		elif user_input2 in lang4:
			frenchtospanish(your_text)
		else:
			print("Enter a correct language")
	elif user_input1 in lang4:
		if user_input2 in lang1:
			spanishtoenglish(your_text)
		elif user_input2 in lang2:
			print('Sorry, spanish to german not supported')
		elif user_input2 in lang3:
			spanishtofrench(your_text)
		else:
			print("Enter a correct language")
	else:
		print("Enter a correct language")


def englishtogerman(your_text):
	"""Function takes user text in English and convert it in german using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-de')
	translation = translation_response.get_result()
	etg_translation = translation['translations'][0]['translation']
	print(etg_translation)

def germantoenglish(your_text):
	"""Function takes user text in German and convert it in English using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='de-en')
	translation = translation_response.get_result()
	gte_translation = translation['translations'][0]['translation']
	print(gte_translation)

def englishtofrench(your_text):
	"""Function takes user text in English and convert it in french using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-fr')
	translation = translation_response.get_result()
	etf_translation = translation['translations'][0]['translation']
	print(etf_translation)

def frenchtoenglish(your_text):
	"""Function takes user text in French and convert it in English using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='fr-en')
	translation = translation_response.get_result()
	fte_translation = translation['translations'][0]['translation']
	print(fte_translation)

def englishtospanish(your_text):
	"""Function takes user text in English and convert it in Spanish using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-es')
	translation = translation_response.get_result()
	ets_translation = translation['translations'][0]['translation']
	print(ets_translation)

def spanishtoenglish(your_text):
	"""Function takes user text in Spanish and convert it in English using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='es-en')
	translation = translation_response.get_result()
	ste_translation = translation['translations'][0]['translation']
	print(ste_translation)

def germantofrench(your_text):
	"""Function takes user text in German and convert it in French using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='de-fr')
	translation = translation_response.get_result()
	gtf_translation = translation['translations'][0]['translation']
	print(gtf_translation)

def frenchtogerman(your_text):
	"""Function takes user text in French and convert it in German using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='fr-de')
	translation = translation_response.get_result()
	ftg_translation = translation['translations'][0]['translation']
	print(ftg_translation)

def germantospanish(your_text):
	"""Function takes user text in German and convert it in Spanish using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='de-es')
	translation = translation_response.get_result()
	gts_translation = translation['translations'][0]['translation']
	print(gts_translation)

def frenchtospanish(your_text):
	"""Function takes user text in French and convert it in Spanish using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='fr-es')
	translation = translation_response.get_result()
	fts_translation = translation['translations'][0]['translation']
	print(fts_translation)

def spanishtofrench(your_text):
	"""Function takes user text in Spanish and convert it in French using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='es-fr')
	translation = translation_response.get_result()
	stf_translation = translation['translations'][0]['translation']
	print(stf_translation)

def spanishtogerman(your_text):
	"""Function takes user text in Spanish and convert it in German using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='es-de')
	translation = translation_response.get_result()
	stg_translation = translation['translations'][0]['translation']
	print(stg_translation)

translator()
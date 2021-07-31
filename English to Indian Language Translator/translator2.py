"""
Translates user input from english language to other indian languages
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
lang2 = ["hindi", "Hindi", "HINDI"]
lang3 = ["gujarati", "Gujarati", "GUJARATI"]
lang4 = ["malayalam", "Malayalam", "MALAYALAM"]
lang5 = ["tamil", "Tamil", "TAMIL"]
lang6 = ["telugu", "Telugu", "TELUGU"]
lang7 = ["urdu", "Urdu", "URDU"]

def translator_new():
	user_input = input("Enter to which language you want to convert: ")
	your_text = input("enter: ")
	if user_input in lang2:
		englishtohindi(your_text)
	elif user_input in lang3:
		englishtogujarati(your_text)
	elif user_input in lang4:
		englishtomalayalam(your_text)
	elif user_input in lang5:
		englishtotamil(your_text)
	elif user_input in lang6:
		englishtotelugu(your_text)
	elif user_input in lang7:
		englishtourdu(your_text)
	else:
		print("Enter a correct language")

def englishtohindi(your_text):
	"""Function takes user text in English and convert it in Hindi using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-hi')
	translation = translation_response.get_result()
	eth_translation = translation['translations'][0]['translation']
	print(eth_translation)

def englishtogujarati(your_text):
	"""Function takes user text in English and convert it in german using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-gu')
	translation = translation_response.get_result()
	etg_translation = translation['translations'][0]['translation']
	print(etg_translation)

def englishtomalayalam(your_text):
	"""Function takes user text in English and convert it in Malayalam using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-ml')
	translation = translation_response.get_result()
	etm_translation = translation['translations'][0]['translation']
	print(etm_translation)

def englishtotamil(your_text):
	"""Function takes user text in English and convert it in Tamil using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-ta')
	translation = translation_response.get_result()
	etta_translation = translation['translations'][0]['translation']
	print(etta_translation)

def englishtotelugu(your_text):
	"""Function takes user text in English and convert it in Telugu using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-te')
	translation = translation_response.get_result()
	ette_translation = translation['translations'][0]['translation']
	print(ette_translation)

def englishtourdu(your_text):
	"""Function takes user text in English and convert it in Urdu using Watson Language Translator"""
	translation_response = language_translator.translate(text=your_text, model_id='en-ur')
	translation = translation_response.get_result()
	etu_translation = translation['translations'][0]['translation']
	print(etu_translation)

translator_new()

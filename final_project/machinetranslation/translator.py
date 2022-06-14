from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION ='2018-05-01'

authenticator = IAMAuthenticator('bnk0jawzGOKA_4tYgrpPRM4gBgxtaAj8ssyNbebxG97K')
language_translator = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
language_translator.set_service_url('https://api.eu-gb.language-translator.\
    watson.cloud.ibm.com/instances/0dd1a3ee-b484-4ad4-9133-df0ed1c4ad9a')

def english_to_french(english_text):
    """Translates English to French"""
    frenchtranslation = language_translator.translate(text=english_text,
    model_id='en-fr').get_result()
    # return frenchtranslation.get("translations")[0].get("translate")
    return frenchtranslation["translations"][0]["translation"]

def french_to_english(french_text):
    """Transalates French to English"""
    englishtranslation = language_translator.translate(text=french_text,
    model_id='fr-en').get_result()
    return englishtranslation["translations"][0]["translation"]

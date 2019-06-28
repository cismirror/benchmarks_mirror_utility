from imbox import Imbox
import config

def get_url():
	with Imbox(config.EMAIL['imap_server'],
                username=config.EMAIL['username'],
                password=config.EMAIL['password'],
		ssl=True,
		ssl_context=None,
		starttls=False) as imbox:
		
		unread_messages = imbox.messages(unread=True)
		
		for uid, message in unread_messages:
			url = message.body['plain'][0].split('Access PDFs (')[1].split(' )')[0] 
			imbox.mark_seen(uid)
			return url
		return None


def mark_all_as_seen():
	with Imbox(config.EMAIL['imap_server'],
                username=config.EMAIL['username'],
                password=config.EMAIL['password'],
		ssl=True,
		ssl_context=None,
		starttls=False) as imbox:
		
		unread_messages = imbox.messages(unread=True)
		
		for uid, message in unread_messages:
			imbox.mark_seen(uid)

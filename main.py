from slackclient import SlackClient


SLACK_TOKEN = 'my_token'
sc = SlackClient(SLACK_TOKEN)

if __name__ == '__main__':

	def send():
		
		sc.api_call(
			"chat.postMessage",
			channel="#my_channel",
			text="This is a test message :smile:"
		)
	
	send()


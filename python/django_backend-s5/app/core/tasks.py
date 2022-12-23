
import json
import requests
from app.celery import app


@app.task(name="unsync_notify")
def unsync_notify(name):
    
    web_hook_url = 'https://hooks.slack.com/services/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'

    slack_msg = {
	"fallback": "....",
	"color": "#36a64f", 
	"fields": [
		{
			"title": "Notification", 
			"value": f"User {name} has been created successfully",
			"short": False
		}
	]

}

    requests.post(web_hook_url, data=json.dumps(slack_msg))

    return 'unsync_notify to slack successfully'
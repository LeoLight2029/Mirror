# discord-message-mirror-cloner
it will send messages from a channel to another via a webhook!

/!\ if you want to use a bot token instead of a user token, replace `bot=False` by `bot=True` in the last line of the script

#### Doc for message_mirror_multi.py

This script allows to use mirror multiple channels with only 1 instance of the script running (and it works even with just 1 channel being mirrored)  
I recommend using this script over message_mirror.py

Open the script and input your token, as well as the blacklisted webhooks (if any, see below for more infos), and the mirrored channels and corresponding webhooks in the dict.  
For python newbies, here is how the dict works
```python
{
111111111111111111: "webhook_url_1",
222222222222222222: "webhook url 2",
700475955574997005: "https://discordapp.com/api/webhooks/578257910442885181/Jgfig2bKJaaXHf_JE3a3_-uEYNI63fttFkr_vxhHCSX40kUmHNstDFcsNN-druADIdds",
}
```  
When a message gets sent in the channel with the id 111111111111111111, this message will be forwarded to the webhook with the url webhook_url_1  
To add a mirrored channel, simply add a new line with the channel id (without quotes), :, and the webhook url (between quotes). Also don't forget to add a , at the end of the line


#### Doc for message_mirror.py

open it by calling it like this: 

`python "message_mirror.py" [id of channel to mirror] "[webhook token]"`


ex: `python "message_mirror.py" 578257710013874186 "https://discordapp.com/api/webhooks/578257910442885181/Jgfig2bKJaaXHf_JE3a3_-uEYNI63fttFkr_vxhHCSX40kUmHNstDFcsNN-druADIdds"`


#### About blacklisted webhoooks
If you want to make a thing that mirror messages both way, just add another line but using the other channel's id and the a webhook in the other channel<br/>
If you do that you'll also need to add the webhooks to the blacklist:<br/>
to do that, edit your py file and replace idofwebhook1 and idofwebhook2 by the ids of the webhooks<br/>
the ids of the webhooks are the numbers after "https://discordapp.com/api/webhooks/". For exemple, the id of the webhook "https://discordapp.com/api/webhooks/578257910442885181/Jgfig2bKJaaXHf_JE3a3_-uEYNI63fttFkr_vxhHCSX40kUmHNstDFcsNN-druADIdds" would be 578257910442885181.<br/>
The line should look like this: blacklistedwebhook = [631928126376599440, 631931858839128064]

Based on a code from [DeadBread](https://github.com/DeadBread76)

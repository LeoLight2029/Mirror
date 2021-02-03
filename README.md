# discord-message-mirror-cloner
it will send messages from a channel to another via a webhook!

/!\ if you want to use a bot token instead of a user token, replace `bot=False` by `bot=True` in the last line of the script

open it by calling it like this: 

`python "message_mirror.py" [id of channel to mirror] "[webhook token]"`


ex: `python "message_mirror.py" 578257710013874186 "https://discordapp.com/api/webhooks/578257910442885181/Jgfig2bKJaaXHf_JE3a3_-uEYNI63fttFkr_vxhHCSX40kUmHNstDFcsNN-druADIdds"`

If you want to make a think that mirror messages both way, just add another line but using the other channel's id and the a webhook in the other channel<br/>
If you do that you'll also need to add the webhooks to the blacklist:<br/>
to do that, edit your py file and replace idofwebhook1 and idofwebhook2 by the ids of the webhooks<br/>
the ids of the webhooks are the numbers after "https://discordapp.com/api/webhooks/". For exemple, the id of the webhook "https://discordapp.com/api/webhooks/578257910442885181/Jgfig2bKJaaXHf_JE3a3_-uEYNI63fttFkr_vxhHCSX40kUmHNstDFcsNN-druADIdds" would be 578257910442885181.<br/>
The line should look like this: blacklistedwebhook = [631928126376599440, 631931858839128064]

Based on a code from [DeadBread](https://github.com/DeadBread76)

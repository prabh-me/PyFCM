from pyfcm import FCMNotification

push_service = FCMNotification(api_key="") #Enter API key

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "" #Enter Reg ID of the user.
data_message = {
    "notificationId": "inactivity", #Should be unique for a notification.
    "source": "firebase",
    "addTags": ["4DayInactive"]  #Place tag to the user

}

result = push_service.notify_single_device(registration_id=registration_id, data_message=data_message)
print result

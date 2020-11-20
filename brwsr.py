import webbrowser

response=webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox",new=2)
print response.text

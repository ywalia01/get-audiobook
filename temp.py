import requests

doc = requests.get("https://ipaudio.club/wp-content/uploads/GOLN/Titan's%20Curse/01.mp3")
file = 'sample.mp3'
with open(file, 'wb') as f:
    f.write(doc.content)

file.flush()
file.close()
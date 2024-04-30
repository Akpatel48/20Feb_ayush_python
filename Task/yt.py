from pytube import YouTube
url=input("enter url:")
#a=YouTube(url).streams.first().codecs.copy().remove()
#d=YouTube(a).streams.first().download()
print(YouTube(url).title)
#u=YouTube(url).metadata.metadata.remove(url)
YouTube(url).streams.first().download()
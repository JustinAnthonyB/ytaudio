# import pafy


# vid = pafy.new(url)

# audiostreams = vid.audiostreams
# for i in audiostreams:
#     print(i.get_filesize())

# audiostreams[3].download()
# print("Success!")


import pafy 

url = input("Enter the url :")
video = pafy.new(url) 

bestaudio = video.getbestaudio() 
bestaudio.download() 

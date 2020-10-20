# Download the best quality Youtube video

import pafy 

url = input("Enter the url :")
video = pafy.new(url) 

streams = video.streams 
for i in streams: 
	print(i) 
	
# get best resolution regardless of format 
best = video.getbest() 

print(best.resolution, best.extension) 

# Download the video 
best.download() 

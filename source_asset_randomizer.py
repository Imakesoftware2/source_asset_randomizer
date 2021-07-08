import os
import sys
import random
import shutil
textures = []
mp3s = []
waves = []

audio_dir = './sounds' 
texture_dir = './textures'
mode = sys.argv[1]

def randasset(assetlist):
	return assetlist[random.randint(0,len(assetlist)-1)]

if mode == 'texture':
	cur_dir = texture_dir
elif mode == 'audio':
	cur_dir = audio_dir

for root, dirs, files in os.walk(cur_dir, topdown=False):
	for name in files:
		if mode == 'texture':
			if name.endswith('.vtf'):
				textures.append( os.path.join(root, name).replace(cur_dir,'') )
		elif mode == 'audio':
			if name.endswith('.wav'):
				waves.append( os.path.join(root, name).replace(cur_dir,'') )
			elif name.endswith('.mp3'):
				mp3s.append( os.path.join(root, name).replace(cur_dir,'') )


	#for name in dirs:
	#	print(os.path.join(root, name))

if mode == 'texture':
	for mat in textures:
		os.makedirs('./hl2'+os.path.dirname(mat),exist_ok=True )
		shutil.copy2(cur_dir+randasset(textures),'./hl2'+mat)

elif mode == 'audio':
	for wav in waves:
		os.makedirs('./hl2'+os.path.dirname(wav),exist_ok=True )
		shutil.copy2(cur_dir+randasset(waves),'./hl2'+wav)

	for mp3 in mp3s:
		os.makedirs('./hl2'+os.path.dirname(mp3),exist_ok=True )
		shutil.copy2(cur_dir+randasset(mp3s),'./hl2'+mp3)


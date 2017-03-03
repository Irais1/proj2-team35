from pydub import AudioSegment

song = [
AudioSegment.from_wav("Afraid.wav"),
AudioSegment.from_wav("tearinmyheart.wav"),
AudioSegment.from_wav("riverflowsinyou.wav")]
ten_seconds = 10 * 1000
mash = []
for one in song:
	first_10_seconds = one[:10000]
	#maybe_middle = one[-70:30]
	last_5_seconds = one[-500:]
# boost volume by 6dB
	beginning = first_10_seconds + 6

# reduce volume by 3dB
	end = last_5_seconds - 3

	without_the_middle = beginning + end
#AudioSegments are immutable

# song is not modified
	backwards = one.reverse()
#Crossfade (again, beginning and end are not modified)

# 1.5 second crossfade
	with_style = beginning.append(end, crossfade=15)
#Repeat

# repeat the clip twice
	do_it_over = with_style * 2
#Fade (note that you can chain operations because everything returns an AudioSegment)

# 2 sec fade in, 3 sec fade out
	awesome = do_it_over.fade_in(20).fade_out(3000)
	#awesome = do_it_over.fade_in(20).fade_out(3000)
	mash.append(awesome)
new_song = AudioSegment.empty()
for i in mash:
	new_song += i

new_song.export("mashup2.wav", format="wav")
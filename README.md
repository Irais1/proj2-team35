Music Mash-Up
Irais Gopar, Jashmae Baculpo, Carolina Pantoja 
CST-205
03-15-17
Link to GitHub repo:https://github.com/Irais1/proj2-team35.git
Link to C9
Coleman

Music Mash-Up is a web application wich grabs 3 audio files from the user and mashes the songs together to creat a new audio file. The user can than listen to the mix of their three audio choices. 

The connect.py does runs but there is a problem with the html and a python file connection. 
If only proj2.html is opened without using connect, it loads an audio. 
There was a bug with the src of the audio, it grabs the correct path, but it doesn’t load into html tag for that reason the files are already loaded and only work if the file is running. 
Python code apart for html does run. Using audio was the problem. 
Songs do mix into one song using beats.py which uses pydub library. 
All songs need to be in the same file in order for beats.py to run. 
The main bug was connecting html and python library else everything else works accordingly. 

						Works Cited
"Custom Progress Bar for and HTML5 Elements." Javascript - Custom Progress Bar for and HTML5 Elements - Stack Overflow. N.p., n.d. Web. 18 Mar. 2017. <http://stackoverflow.com/questions/12314345/custom-progress-bar-for-audio-and-progress-html5-elements>.
"How to Upload & Save Files with Desired Name." Php - How to Upload & Save Files with Desired Name - Stack Overflow. N.p., n.d. Web. 18 Mar. 2017. <http://stackoverflow.com/questions/3509333/how-to-upload-save-files-with-desired-name>.
"HTML Color Names." HTML Color Names. N.p., n.d. Web. 18 Mar. 2017. <https://www.w3schools.com/colors/colors_names.asp>.
"HTML Tag." HTML Button Tag. N.p., n.d. Web. 18 Mar. 2017. <https://www.w3schools.com/tags/tag_button.asp>.
"HTML Tag." HTML Button Tag. N.p., n.d. Web. 18 Mar. 2017. <https://www.w3schools.com/tags/tag_button.asp>.
"HTML5 Audio Clicking the Progress Bar to Move to a Different Time." Javascript - HTML5 Audio Clicking the Progress Bar to Move to a Different Time - Stack Overflow. N.p., n.d. Web. 18 Mar. 2017. <http://stackoverflow.com/questions/11706177/html5-audio-clicking-the-progress-bar-to-move-to-a-different-time>.
Jiaaro. "Jiaaro/pydub." GitHub. N.p., 17 Feb. 2017. Web. 18 Mar. 2017. <https://github.com/jiaaro/pydub>.
Jiaaro. "Jiaaro/pydub." GitHub. N.p., n.d. Web. 18 Mar. 2017. <https://github.com/jiaaro/pydub/blob/master/API.markdown>.
"Pydub by Jiaaro." Jiaaro/pydub @ GitHub. N.p., n.d. Web. Mar. 2017. <http://pydub.com/>.

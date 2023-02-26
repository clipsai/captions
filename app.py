# from flask import Flask, request, render_template, send_file

# import subprocess

# app = Flask(__name__)

# @app.route("/")
# def hello():
# 	return "Hello World!"

# @app.route("/caption", methods=['GET', 'POST'])
# def caption():
# 	if request.method == 'POST':
# 		print("Starting...")
# 		video_file = request.files['video']
# 		srt_file = request.files['srt']
# 		font_size = int(request.form.get('font_size'))
# 		font_name = request.form.get('font_name')
# 		font_color = 'FF00F6E0'

# 		video_file.save('homelander.mp4')
# 		srt_file.save('homeSubs.srt')

# 		# Set the names of the input video and subtitle files
# 		input_video = 'homelander.mp4'
# 		subtitles = 'homeSubs.srt'

# 		# Set the name of the output video file
# 		output_video = 'output_video.mp4'

# 		# Set the font options for the subtitles
# 		# font_size = 20
# 		# font_color = 'black'
# 		# font_name = 'Arial'

# 		# Run the ffmpeg command to add the subtitles to the video
# 		subprocess.run(['ffmpeg', '-i', input_video, '-vf', f'subtitles={subtitles}:force_style=\'Fontname={font_name},Fontsize={font_size},Fontcolor=&{font_color}\'', output_video])
# 		return send_file('output_video.mp4', mimetype='video/mp4')

# 	return render_template('form.js')

# if __name__ == "__main__":
# 	app.run()

from flask import Flask, request, render_template, send_file
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/caption", methods=['GET', 'POST'])
def caption():
    if request.method == 'POST':
        print("Starting...")
        video_file = request.files['video']
        srt_file = request.files['srt']
        font_size = int(request.form.get('font_size'))
        font_name = request.form.get('font_name')
        font_color = 'FF00F6E0'

        video_file.save('homelander.mp4')
        srt_file.save('homeSubs.srt')

        # Set the names of the input video and subtitle files
        input_video = 'homelander.mp4'
        subtitles = 'homeSubs.srt'

        # Set the name of the output video file
        output_video = 'output_video.mp4'

        # Set the font options for the subtitles
        # font_size = 20
        # font_color = 'black'
        # font_name = 'Arial'

        # Run the ffmpeg command to add the subtitles to the video
        subprocess.run(['ffmpeg', '-i', input_video, '-vf', f'subtitles={subtitles}:force_style=\'Fontname={font_name},Fontsize={font_size},Fontcolor=&{font_color}\'', output_video])
        return send_file('output_video.mp4', mimetype='video/mp4')

    return render_template('form.html')

if __name__ == "__main__":
    app.run()

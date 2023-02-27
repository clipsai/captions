from flask import Flask, request, render_template, send_file, url_for
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def caption():
    if request.method == 'POST':
        # Get the user's inputs
        video_file = request.files['video']
        srt_file = request.files['srt']
        font_size = int(request.form.get('font_size'))
        font_name = request.form.get('font_name')
        font_color = 'FF00F6E0'

        # Save the uploaded files to disk
        video_file.save('input_video.mp4')
        srt_file.save('input_subtitles.srt')

        # Encode the video with subtitles
        input_video = 'input_video.mp4'
        subtitles = 'input_subtitles.srt'
        output_video = os.path.join(app.root_path, 'static/output_video.mp4')
        subprocess.run(['ffmpeg', '-i', input_video, '-vf', f'subtitles={subtitles}:force_style=\'Fontname={font_name},Fontsize={font_size},Fontcolor=&{font_color}\'', output_video])

        # Check if the output video file was created successfully
        if os.path.exists(output_video):
            video_url = url_for('static', filename='output_video.mp4')
            return render_template('video.html', video_url=video_url)
        else:
            return "Error: Failed to encode video with subtitles."

    return render_template('form.html')

if __name__ == "__main__":
    app.run()


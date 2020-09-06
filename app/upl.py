import os
from functools import wraps
from flask import render_template, send_file, abort, send_from_directory
from app import UPL, app




@app.route('/file-downloads/')
def file_downloads():
	try:
		return render_template('upl.html')
	except Exception as e:
		return str(e)

@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file('stress/IGORRR - DOWNGRADE DESERT.mp4',add_etags=True, attachment_filename='IGORRR - DOWNGRADE DESERT.mp4')
		#return send_from_directory('stress/IGORRR - DOWNGRADE DESERT.mp4', as_attachment=True)
	except Exception as e:
		return str(e)
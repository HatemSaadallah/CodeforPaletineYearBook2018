from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/yearOne')
def year_one():
	return render_template("y1_page.html")

@app.route('/yearTwo')
def year_two():
	return render_template("y2_page.html")

@app.route('/yearThree')
def year_three():
	return render_template("y3_page.html")


@app.route('/faculty')
def faculty():
	return render_template("faculty.html")

if __name__ == '__main__':
	app.run(debug = True)
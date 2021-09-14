from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/")
@app.route("/signup")
def signup():
	return render_template("sign_up.html")


@app.route("/feedback", methods=["POST"])
def feedbackform():
	return render_template("end.html")

	

@app.route("/thankyou", methods=["POST"])
def thankyou():
	return render_template("thank.html")



if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
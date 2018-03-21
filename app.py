import os

from flask import Flask, render_template, request

app = Flask("my_first_app")


@app.route("/")
def say_hello():
    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def get_feedback():
      # request.values is a dictionary holding any
      # POST request data that's not already part of the URL
  data = request.values

  return render_template("feedback.html", form_data=data)


# Passing in "debug=True" as an (keyword) argument to app.run(...) will make your Flask powered
# server/application refreshes automatically when you make any changes to this file.
"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at https://www.heroku.com/ before the deployment session!). When
running the app on Heroku, the PORT environment/config variable is pre-populated by
Heroku to tell our app the correct port to run on.
"""
if "PORT" in os.environ:
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
    app.run(debug=True)

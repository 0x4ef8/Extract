from flask import Flask, render_template, request, redirect, url_for
from scraper import TimelineNoLogin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    id_type = request.form['type']
    fb_id = request.form['fb_id']
    limit = int(request.form['limit'])

    if id_type == 'group':
        scraper = TimelineNoLogin()
        scraper.LandingTimeline(id_type='group', id=fb_id, limit=limit)
    else:
        scraper = TimelineNoLogin()
        scraper.LandingTimeline(id_type='page', id=fb_id, limit=limit)

    result = scraper.result
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

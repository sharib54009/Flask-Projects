from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("Data\stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route('/')
def home():
    return render_template('home.html', data=stations.to_html())


@app.route('/api/v1/<station>/<date>')
def about(station, date):

    filename = "Data/TG_STAID" + str(station).zfill(6) + ".txt"

    df = pd.read_csv(
        filename,
        skiprows=30,
        names=["STAID", "SOUID", "DATE", "TG", "Q_TG"]
    )

    df["DATE"] = pd.to_datetime(df["DATE"], format="%Y%m%d")

    date = pd.to_datetime(date)

    temperature = df.loc[df["DATE"] == date, "TG"].squeeze() / 10

    return {
        "station": station,
        "date": date.strftime("%Y-%m-%d"),
        "temperature": float(temperature)
    }
    
@app.route('/api/v1/<station>')
def all_data(station):
    filename = "Data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(
            filename,
            skiprows=30,
            names=["STAID", "SOUID", "DATE", "TG", "Q_TG"]
        )
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "Data/TG_STAID" + str(station).zfill(6) + ".txt"
    
    df = pd.read_csv(
            filename,
            skiprows=19,
            names=["STAID", "SOUID", "DATE", "TG", "Q_TG"]
        )
    df['    DATE'] = df["    DATE"].astype(str)
    result = df[df['    DATE'].startswith(str(year))]
    return result

    
    


if __name__ == '__main__':
    app.run(debug=True)
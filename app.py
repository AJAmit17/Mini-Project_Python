from flask import Flask, redirect, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

## Load DataSet
df = pd.read_csv('spotify-2023.csv',encoding="latin-1")


### top Artist By Year
def top_streamed_artist_by_year(df, year):
    """
    df : DataFrame
    year : int
    """
    
    df['released_year'] = pd.to_datetime(df['released_year'], format='%Y')

    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    df = df.dropna(subset=['streams'])

    df_year = df[df['released_year'].dt.year == year]

    top_artists_year = df_year.groupby('artist(s)_name').agg({'streams':'sum'}).reset_index().sort_values('streams', ascending=False).head()

    plt.figure(figsize=(15, 8))
    sns.set(style='whitegrid')

    ax = sns.barplot(x='artist(s)_name', y='streams', data=top_artists_year, width=0.6)
    plt.xlabel('Artist', fontweight='bold')
    plt.ylabel('Stream Count', fontweight='bold')
    plt.title(f'The Top 5 Most Streamed Artists in {year}', fontsize=18, fontweight='bold')
    
    # Save the plot to a file (optional)
    plot_filename = f'static/top_artists_{year}.png'
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()

    return plot_filename


### Songs By Year
def top_streamed_songs_by_year(df, year):
    """
    df: DataFrame
    year: int
    """
    top_songs = df[df['released_year'] == year][['track_name', 'streams']].sort_values('streams', ascending=False).head()

    plt.figure(figsize=(15, 8))
    sns.set(style='whitegrid')

    top_songs['streams'] = pd.to_numeric(top_songs['streams'], errors='coerce')

    ax = sns.barplot(x='track_name', y='streams', data=top_songs, order=top_songs['track_name'], width=0.6)
    plt.xlabel('Song', fontweight='bold')
    plt.ylabel('Stream Count', fontweight='bold')
    plt.title(f'The Top 5 Most Streamed Songs in {year}', fontsize=18, fontweight='bold')

    plot_filename = f'static/top_songs_{year}.png'
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()

    print(f"Image saved to: {plot_filename}")

    return plot_filename


### OVerall top Songs
def overall_top_songs(df):
    """
    df: DataFrame
    """
    top_songs = df[['track_name', 'streams']].sort_values('streams', ascending=False).head()

    plt.figure(figsize=(15, 8))
    sns.set(style='whitegrid')

    ax = sns.barplot(x='track_name', y='streams', data=top_songs, width=0.6)
    plt.xlabel('Song', fontweight='bold')
    plt.ylabel('Stream Count', fontweight='bold')
    plt.title('The Overall Top 5 Most Streamed Songs', fontsize=18, fontweight='bold')

    plot_filename = 'static/overall_top_songs.png'
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()

    return plot_filename


### 0verAll top artist
def overalll_top_artist(df):
    """
    df : Dataframe
    """
    top_artists = df.groupby('artist(s)_name').agg({'streams':'sum'}).reset_index().sort_values('streams', ascending=False).head()

    plt.figure(figsize=(15, 8))
    sns.set(style='whitegrid')

    ax = sns.barplot(x='artist(s)_name', y='streams', data=top_artists,width=0.6)
    plt.xlabel('Artist',fontweight='bold')
    plt.ylabel('Stream Count',fontweight='bold')
    plt.title('The Top 5 Most Streamed Artists',fontsize=18, fontweight='bold')

    plot_filename = f'static/top_artists.png'
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()

    return plot_filename


### Flask Application
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def reuslts():
    choice = request.form.get('choice')
    
    # top artist by year
    if int(choice) == 1:
        year = request.form.get('year')
        plot_filename = top_streamed_artist_by_year(df, int(year))
        return render_template('result.html', year=year, plot_filename=plot_filename)
    
    #top songs by year
    elif int(choice) == 2:
        song_year = request.form.get('year')
        plot_filename = top_streamed_songs_by_year(df, int(song_year))
        return render_template('result.html', year=song_year, plot_filename=plot_filename)
    
    elif int(choice) == 3:
        plot_filename = overall_top_songs(df)
        return render_template('result.html', plot_filename=plot_filename)
    
    elif int(choice) == 4:
        plot_filename = overalll_top_artist(df)
        return render_template('result.html', plot_filename=plot_filename)
        
    else:
        msg = "<p>Wrong input please re-enter your choice</p>"
        return msg
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
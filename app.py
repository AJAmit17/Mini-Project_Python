from flask import Flask, render_template, request
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load DataSet
df = pd.read_csv('spotify-2023.csv', encoding="latin-1")

### top Artist By Year
def top_streamed_artist_by_year(df, year):
    """
    df : DataFrame
    year : int (YYYY)
    """
    # Create a copy of the DataFrame
    df_copy = df.copy()

    df_copy['streams'] = pd.to_numeric(df_copy['streams'], errors='coerce')
    df_copy = df_copy.dropna(subset=['streams'])

    df_year = df_copy[df_copy['released_year'] == year]

    top_artists_year = df_year.groupby('artist(s)_name').agg({'streams':'sum'}).reset_index().sort_values('streams', ascending=False).head()

    plt.figure(figsize=(15, 8))
    sns.set(style='whitegrid')

    ax = sns.barplot(x='artist(s)_name', y='streams', data=top_artists_year, width=0.6)
    plt.xlabel('Artist', fontweight='bold')
    plt.ylabel('Stream Count', fontweight='bold')
    plt.title(f'The Top 5 Most Streamed Artists in {year}', fontsize=18, fontweight='bold')

    plot_filename = f'static/top_artists_{year}.png'
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()

    return plot_filename

### Songs By Year
def top_streamed_songs_by_year(df, year):
    """
    df: DataFrame
    year: int (YYYY)
    """
    # Create a copy of the DataFrame
    df_copy = df.copy()

    df_copy['streams'] = pd.to_numeric(df_copy['streams'], errors='coerce')
    df_copy = df_copy.dropna(subset=['streams'])

    df_year = df_copy[df_copy['released_year'] == year]

    top_songs = df_year.sort_values('streams', ascending=False).head()

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

    return plot_filename

### Overall top Songs
def overall_top_songs(df):
    """
    df: DataFrame
    """
    # Create a copy of the DataFrame
    df_copy = df.copy()

    df_copy['streams'] = pd.to_numeric(df_copy['streams'], errors='coerce')
    df_copy = df_copy.dropna(subset=['streams'])

    top_songs = df_copy.sort_values('streams', ascending=False).head()

    plt.figure(figsize=(15, 8))
    sns.set(style='whitegrid')

    ax = sns.barplot(x='track_name', y='streams', data=top_songs, palette='viridis', width=0.6)
    plt.xlabel('Song', fontweight='bold')
    plt.ylabel('Stream Count', fontweight='bold')
    plt.title('The Overall Top 5 Most Streamed Songs', fontsize=18, fontweight='bold')

    plot_filename = 'static/overall_top_songs.png'
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()

    return plot_filename

### Overall top artist
def overall_top_artist(df):
    """
    df : DataFrame
    """
    # Create a copy of the DataFrame
    df_copy = df.copy()

    df_copy['streams'] = pd.to_numeric(df_copy['streams'], errors='coerce')
    df_copy = df_copy.dropna(subset=['streams'])

    top_artists = df_copy.groupby('artist(s)_name')['streams'].sum().reset_index().sort_values('streams', ascending=False).head()

    plt.figure(figsize=(15, 8))
    sns.set(style='whitegrid')

    ax = sns.barplot(x='artist(s)_name', y='streams', data=top_artists, palette='viridis', ci=None, width=0.6)
    plt.xlabel('Artist', fontweight='bold')
    plt.ylabel('Stream Count', fontweight='bold')
    plt.title('The Top 5 Most Streamed Artists', fontsize=18, fontweight='bold')

    plot_filename = 'static/overall_top_artists.png'
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()

    return plot_filename

### Flask Application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def results():
    choice = request.form.get('choice')

    # top artists by year
    if int(choice) == 1:
        year = request.form.get('year')
        plot_filename = top_streamed_artist_by_year(df, int(year))
        return render_template('result.html', year=year, plot_filename=plot_filename)

    # top songs by year
    elif int(choice) == 2:
        song_year = request.form.get('year')
        plot_filename = top_streamed_songs_by_year(df, int(song_year))
        return render_template('result.html', year=song_year, plot_filename=plot_filename)

    # overall top songs
    elif int(choice) == 3:
        plot_filename = overall_top_songs(df)
        return render_template('result.html', plot_filename=plot_filename)

    # overall top artists
    elif int(choice) == 4:
        plot_filename = overall_top_artist(df)
        return render_template('result.html', plot_filename=plot_filename)

    else:
        return render_template('no_result.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
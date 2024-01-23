<h1 align="center">Spotify Analytics Web App</h1>

<p align="center">
  Welcome to the Spotify Analytics Web App! This application provides insights into Spotify streaming data, allowing users to explore the most streamed artists and songs.
</p>

## Prerequisites

- Python 3.9
- Flask
- Pandas
- Seaborn
- Matplotlib

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/spotify-analytics-web-app.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd spotify-analytics-web-app
    ```

3. **Create and activate a virtual environment (recommended):**

    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open a web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the application.**

3. **Choose an option from the dropdown menu to view streaming analytics:**
   - *Top Streamed Artists by Year*
   - *Top Streamed Songs by Year*
   - *Overall Top Streamed Songs*
   - *Overall Top Streamed Artists*

4. **Follow the on-screen instructions to provide additional input such as the target year.**

5. **View the generated visualizations and explore Spotify streaming insights.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Dataset Source:** [Top Spotify Songs 2023](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023)
- This project was created for educational purposes and to explore data visualization using Flask and Seaborn.

Feel free to contribute, report issues, or provide suggestions to make this application even better!

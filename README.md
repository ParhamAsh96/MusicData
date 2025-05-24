# 🎧 Music Popularity Analyzer

This is a personal project created as part of my first-year coursework in Software Engineering and Management at the University of Gothenburg. The project leverages multiple public APIs to answer fun and engaging questions about music artists while helping users explore data visualization and even learn English through lyrics.

---

## 📌 Project Goals

This project was built to answer the following questions:

1. **Which artist is more popular?**  
   → Choose two artists from a predefined list and compare their Spotify popularity score.

2. **How many times was the artist searched this year?**  
   → Select an artist and view their monthly Wikipedia search statistics in a line chart.

3. **Wanna learn English in a fun way?**  
   → Pick a song from your favorite artist, and the app will return a random word from the lyrics with a simple definition!

---

## 🛠️ Features & Functionality

- Compare Spotify popularity scores of two artists.
- Visualize monthly Wikipedia search frequency for selected artists.
- Play a lyrics-based game to learn new English vocabulary.
- Simple command-line interface for user interaction.

---

## 🧰 Technologies & Libraries Used

### 🧪 Core Libraries

| Library    | Purpose                                                                  |
| ---------- | ------------------------------------------------------------------------ |
| `requests` | To send HTTP requests to Spotify, Wikipedia, Lyrics, and Dictionary APIs |
| `json`     | Parsing, reading, and writing JSON responses                             |
| `os`       | Handling file operations, e.g., removing downloaded data                 |
| `random`   | Selecting random words from song lyrics                                  |
| `re`       | Extracting words from lyrics using regular expressions                   |

### 📊 Data Processing & Visualization

| Library      | Purpose                                                |
| ------------ | ------------------------------------------------------ |
| `matplotlib` | Creating charts (e.g., Wikipedia monthly search chart) |
| `pandas`     | Required for Wikipedia API + used for structured data  |
| `tabulate`   | Displaying clean, formatted tables in the terminal     |

---

## 🌐 APIs Used

- **Spotify Web API**  
  → For retrieving artist information and popularity scores.

- **Wikipedia API**  
  → For monthly view statistics on artist search frequency.

- **Lyrics.ovh API**  
  → To fetch lyrics of selected songs.

- **DictionaryAPI.dev**  
  → To define random words found in song lyrics.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🙋‍♂️ Author

Made with ❤️ by Parham – Feel free to connect on [LinkedIn](https://www.linkedin.com/in/ali-parham-ashrafzadeh/).

---

# 🌐 **Web Mining Algorithm**

The **Web Mining Algorithm** is a Python-based tool designed to extract, analyze, and visualize information from websites. It leverages web scraping techniques, IP geolocation, and natural language processing to gather data such as location, names, emails, and social media links from a list of target websites.

---

## 🌟 **Key Features**

- **Web Scraping**: Utilizes `requests` and `BeautifulSoup` to fetch and parse website content.
- **IP Geolocation**: Determines the geographical location of websites using IP addresses via the `ipapi.co` API.
- **Named Entity Recognition (NER)**: Employs `spaCy` to identify and extract names from website content.
- **Social Media Link Extraction**: Collects links to social media profiles, including Twitter, Facebook, LinkedIn, Instagram, and YouTube.
- **Email Extraction**: Identifies and extracts email addresses present on the website.
- **Data Presentation**: Outputs the extracted information in a structured table format using `PrettyTable`.

---

## 💻 **Technology Stack**

- **Programming Language**: Python 3.x
- **Libraries**:
  - `requests`
  - `beautifulsoup4`
  - `socket`
  - `spacy`
  - `prettytable`

---

## 🚀 **Getting Started**

### **Prerequisites**

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Install Required Libraries**: Use `pip` to install the necessary libraries:

   ```bash
   pip install requests beautifulsoup4 spacy prettytable
   python -m spacy download en_core_web_sm

## 🚀 **Clone the Repository**

```bash
git clone https://github.com/ozeraysenur/WebMiningAlgorithm.git
cd WebMiningAlgorithm
```

## 🏁 **Run the Script**

### **Prepare Input**
Create a text file named `websites.txt` containing the list of target websites, each on a new line.

### **Execute the Script**
Run the main Python script:

```bash
python main.py
```

### **View Output**
The script will display a table with the extracted information, including website, location, names, emails, and social media links.

---

## 📂 **Repository Structure**

```bash
WebMiningAlgorithm/
├── websites.txt            # Input file containing list of target websites
├── main.py                 # Main script for web mining
├── README.md               # Project documentation
```

---

## 📊 **Example Output**

After running the script, you can expect an output similar to:

```
+-------------------+----------+---------------------+-------------------+-----------+---------+----------+----------+-----------+
|      Website      | Location |        Names        |       Email       | Instagram | YouTube | LinkedIn | Twitter  | Facebook  |
+-------------------+----------+---------------------+-------------------+-----------+---------+----------+----------+-----------+
| somewebsite1.com  |   N/A    | ['Ayse Nur Ozer']   |   contact@site1   |    N/A    |   N/A   |    N/A   |   N/A    |    N/A    |
| somewebsite2.com  |   N/A    | ['John Doe']        |   info@site2      |    N/A    |   N/A   |    N/A   |   N/A    |    N/A    |
+-------------------+----------+---------------------+-------------------+-----------+---------+----------+----------+-----------+
```

---

## 🛠️ **Customization**

- **Adding More Social Media Platforms**: To extend the script's capabilities to extract additional social media links, you can modify the `extract_social_media_links` function in `main.py` to include patterns for other platforms.
- **Enhancing Named Entity Recognition**: To improve the accuracy of name extraction, consider training `spaCy` with a custom dataset tailored to your specific requirements.

---

## 🤝 **Contributions**

Contributions are welcome! To contribute:

1. **Fork the Repository**: Click the 'Fork' button on the GitHub page.

2. **Create a New Branch**: For your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. **Make Changes**: Implement your feature or fix.

4. **Commit Changes**: Commit your modifications with a descriptive message:

   ```bash
   git commit -m "Description of feature or fix"
   ```

5. **Push to Branch**: Push your changes to GitHub:

   ```bash
   git push origin feature-name
   ```

6. **Submit Pull Request**: Open a pull request on GitHub with a detailed description of your changes.

---


## 💡 **Acknowledgements**

Special thanks to the developers and maintainers of the open-source libraries utilized in this project, including `requests`, `BeautifulSoup`, `spaCy`, and `PrettyTable`.

---

For any questions or support, please open an issue in this repository.

*Happy coding!* 💻✨

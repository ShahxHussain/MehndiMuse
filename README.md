# 🌸 MehndiMuse

git 
**MehndiMuse** is a beautiful, AI-powered web app that generates custom Mehndi (Henna) designs for your hands, perfect for Eid and other special occasions! Built with Streamlit and Google Gemini, it lets you personalize every aspect of your Mehndi design and see instant, stunning results.

---

## ✨ Features
- **Multiple Mehndi Styles:** Pakistani, Arabic, Indian, Bridal, Tattoo, and more.
- **Hand Age Selection:** From toddlers to seniors.
- **Occasion Choices:** Eid (default), Wedding, Festival, Party, and more.
- **Complexity Control:** Choose from simple to intricate designs.
- **Custom Text:** Optionally add a name or phrase to be written on the hand.
- **Multiple Images:** Generate up to 10 designs at once (default is 3).
- **Festive UI:** Modern, colorful, and Eid-themed interface with quotes for girls.
- **AI-Powered:** Uses Google Gemini for realistic, creative image generation.

---

## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone URL HERE
cd mehndimuse
```

### 2. **Set Up Python Environment**
- Make sure you have **Python 3.8+** installed.
- (Recommended) Create and activate a virtual environment:
  ```bash
  python -m venv venv
  # On Windows:
  venv\Scripts\activate
  # On macOS/Linux:
  source venv/bin/activate
  ```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Get a Google Gemini API Key**
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create an API key.
- Create a `.env` file in the project root and add:
  ```
  API_KEY=your_gemini_api_key_here
  ```

### 5. **Run the App**
```bash
streamlit run script.py
```
- The app will open in your browser. Enjoy creating Mehndi designs!

---

## 🎨 Customization
- **Colors & Theme:** Easily change the color palette in `script.py` (CSS section) to match your event or brand.
- **Quotes:** Add or edit quotes in the `mehndi_quotes` list for more personalized messages.
- **Default Settings:** Change default occasion, number of images, or complexity in the sidebar widget definitions.

---

## 🙏 Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Google Gemini](https://aistudio.google.com/)
- All the girls and women who love Mehndi and make every festival more beautiful!

---

## 🕌 Eid Mubarak!
Celebrate with style and creativity. Let MehndiMuse color your hands and your celebrations! 
# 🔐 Password Generator GUI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey.svg)

**A modern, secure, and user-friendly password generator with a beautiful GUI**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

- **🎨 Modern Dark UI**: Built with CustomTkinter for a sleek, modern appearance
- **🔧 Customizable Length**: Generate passwords from 4 to 50 characters
- **🎯 Character Options**: Choose from uppercase, lowercase, numbers, and symbols
- **💪 Password Strength**: Real-time strength indicator (Weak to Very Strong)
- **📋 One-Click Copy**: Instant clipboard integration
- **🔄 Easy Reset**: Clear generated passwords with one click
- **⚡ Fast Generation**: Instant password creation
- **🛡️ Secure**: Uses Python's cryptographically secure random module

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShubhieSingh/CodSoft_3.git
   cd CodSoft_3
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python Password_Generator_GUI.py
   ```

### Alternative Installation

```bash
# Install dependencies manually
pip install customtkinter pyperclip

# Run the application
python Password_Generator_GUI.py
```

## 🎯 Usage

1. **Launch the Application**: Run the Python script to open the GUI
2. **Set Password Length**: Use the slider to choose your desired password length (4-50 characters)
3. **Select Character Types**: Check/uncheck the options for:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Symbols (!@#$%^&*)
4. **Generate Password**: Click the "🎲 Generate Password" button
5. **Copy & Use**: Click "📋 Copy to Clipboard" to copy your new password
6. **Clear**: Use "🗑️ Clear" to reset and generate a new password

## 📱 Screenshots

<div align="center">

### Main Interface
![Password Generator Interface](https://via.placeholder.com/500x750/1a1a1a/ffffff?text=Password+Generator+GUI)

*Clean, modern interface with intuitive controls*

### Password Generation
![Generated Password](https://via.placeholder.com/500x100/2d2d2d/00ff00?text=Generated:+Xy9#mK2$pL4@)

*Real-time password generation with strength indicator*

</div>

## 🛠️ Technical Details

### Built With

- **[Python](https://python.org/)** - Core programming language
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Modern GUI framework
- **[Pyperclip](https://github.com/asweigart/pyperclip)** - Clipboard functionality

### Password Strength Algorithm

The strength indicator uses a scoring system based on:
- ✅ Password length (8+, 12+, 16+ characters)
- ✅ Character variety (uppercase, lowercase, numbers, symbols)
- ✅ Real-time evaluation and color-coded feedback

### Security Features

- 🔒 Cryptographically secure random generation
- 🚫 No password storage or logging
- 🛡️ Local-only operation (no network requests)
- 🔐 Immediate clipboard clearing option

## 📁 Project Structure

```
CodSoft_3/
├── Password_Generator_GUI.py    # Main application file
├── requirements.txt             # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/CodSoft_3.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📋 Roadmap

- [ ] 🌐 Add multiple language support
- [ ] 📊 Password history (optional, with encryption)
- [ ] 🎨 Custom themes and color schemes
- [ ] 📱 Mobile-responsive design
- [ ] 🔄 Password expiry reminders
- [ ] 📈 Advanced password analytics

## 🐛 Issues & Support

If you encounter any issues or have suggestions:

1. Check [existing issues](https://github.com/ShubhieSingh/CodSoft_3/issues)
2. [Create a new issue](https://github.com/ShubhieSingh/CodSoft_3/issues/new) with:
   - Operating system
   - Python version
   - Error message (if any)
   - Steps to reproduce

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shubhie Singh**

- GitHub: [@ShubhieSingh](https://github.com/ShubhieSingh)
- Project Link: [https://github.com/ShubhieSingh/CodSoft_3](https://github.com/ShubhieSingh/CodSoft_3)

## 🙏 Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the amazing GUI framework
- [Pyperclip](https://github.com/asweigart/pyperclip) for clipboard functionality
- The Python community for continuous inspiration

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by [Shubhie Singh](https://github.com/ShubhieSingh)

</div>

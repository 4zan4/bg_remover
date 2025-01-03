# 🌟 Background Remover 🎨  

Remove image backgrounds effortlessly using cutting-edge AI technology! This Django-based web application makes it easy to process your images with a clean and intuitive interface. Perfect for professionals, creatives, and developers.  

---
## 👀 Preview
![](https://github.com/4zan4/bg_remover/blob/main/preview/preview%20web.gif)

## ✨ Features  

- 🌈 **Effortless Background Removal**: Upload an image, and the app will remove the background in seconds!  
- 💻 **Modern Web Interface**: Responsive design for seamless use on any device.  
- ⚡ **AI-Powered Processing**: Utilizes ONNX Runtime for fast and accurate results.  
- 🗂️ **Secure File Handling**: Safely upload and download images with ease.  

---

## 🚀 Technologies  

| **Tech**        | **Purpose**                 |  
|------------------|-----------------------------|  
| Django           | Backend Framework          |  
| HTML + CSS       | Frontend Design            |  
| Bootstrap        | UI Framework               |  
| ONNX Runtime     | AI Inference               |  

---

## 🛠️ Setup  

### 📋 Prerequisites  

- Python 3.8+ 🐍  
- Django 4.0+ 🌐  
- ONNX Runtime (`pip install onnxruntime`) 🤖  

### 📥 Installation  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/jong4Dev/Django_bg_remover.git
   cd Django_bg_remover
2. **Set up the environment**:
   ```bash
   python -m venv env
   env\Scripts\activate 
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt  
4. **Run migrations**:
   ```bash
   python manage.py migrate  
5. **Start the server**:
   ```bash
   python manage.py runserver  
6. **Open your browser and navigate to: http://127.0.0.1:8000 🌐**

## 📷 Screenshots
![](preview/scweb.png)

## 📂 File Structure
   ```bash
ai-bg-remover/  
├── ai_bg_remover/           # Main Django project folder  
├── remover/                 # Background removal app  
│   ├── templates/remover/   # HTML templates  
│   ├── static/remover/      # CSS, JS, and other static files  
│   └── views.py             # View logic for uploads
├── requirements.txt         # Dependencies  
└── README.md                # Project documentation  

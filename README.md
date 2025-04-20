# AI Image Generator 🎨

A professional web application built with Streamlit that generates high-quality images using Stable Diffusion based on text prompts. This application provides an intuitive interface for creating AI-generated artwork with advanced customization options.

![AI Image Generator Demo](https://via.placeholder.com/800x400?text=AI+Image+Generator+Demo)

## ✨ Features

- 🖼️ Generate high-quality images from text prompts
- 🚫 Support for negative prompts to exclude unwanted elements
- 🔄 Generate multiple images simultaneously
- 💾 Download generated images in high resolution
- 🎯 Advanced customization options:
  - Image size selection (512x512, 768x768, 1024x1024)
  - Guidance scale adjustment
  - Number of inference steps
  - Style presets (Photographic, Digital Art, Oil Painting, etc.)
- 📝 Built-in prompt writing tips and guidance
- 🎨 User-friendly web interface with real-time preview

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: Stable Diffusion v1.5
- **Dependencies**: PyTorch, Diffusers, Transformers

## 📋 Requirements

- Python 3.8 or higher
- CUDA-capable GPU (recommended) or CPU
- Internet connection for downloading the model
- 8GB+ RAM (16GB recommended)
- 10GB+ free disk space

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ai-image-generator.git
cd ai-image-generator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Use the interface to:
   - Enter your main prompt
   - Add negative prompts (optional)
   - Adjust advanced settings
   - Select image size and style
   - Generate and download images

## 🎨 Tips for Better Results

### Writing Effective Prompts
- Be specific and detailed in your descriptions
- Use descriptive adjectives and adverbs
- Mention the desired style (e.g., 'digital art', 'photograph', 'oil painting')
- Include quality terms (e.g., 'highly detailed', '4k', 'professional')
- Specify lighting conditions (e.g., 'dramatic lighting', 'soft lighting')

### Advanced Settings
- **Guidance Scale**: Higher values (7-12) = More prompt adherence
- **Steps**: More steps (50-75) = Better quality but slower generation
- **Image Size**: Larger sizes = More detail but slower generation

### Common Negative Prompts
- blurry, low quality, distorted
- bad anatomy, bad proportions
- duplicate, watermark, signature
- text, logo, watermark
- extra limbs, missing limbs

## 📝 Notes

- The first run will download the Stable Diffusion model (~4GB)
- Image generation time varies based on hardware:
  - GPU: 10-30 seconds per image
  - CPU: 2-5 minutes per image
- Generated images are automatically saved in the `generated_images` directory

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stable Diffusion](https://stability.ai/stable-diffusion) by Stability AI
- [Streamlit](https://streamlit.io/) for the web interface
- [Hugging Face](https://huggingface.co/) for the model hosting

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/ai-image-generator](https://github.com/yourusername/ai-image-generator) 
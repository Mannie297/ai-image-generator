# Import necessary libraries
import streamlit as st  # For creating the web interface
import torch  # PyTorch for deep learning operations
from diffusers import StableDiffusionPipeline  # For the Stable Diffusion model
from PIL import Image  # For image processing
import os  # For file and directory operations
import time  # For measuring generation time

# Configure the Streamlit page settings
st.set_page_config(
    page_title="AI Image Generator",  # Title shown in browser tab
    page_icon="🎨"  # Emoji icon for the browser tab
)
st.title("AI Image Generator")  # Main title of the application

# Display system information in the sidebar
st.sidebar.title("System Information")
# Show PyTorch version
st.sidebar.write(f"PyTorch version: {torch.__version__}")
# Check if CUDA (GPU) is available
st.sidebar.write(f"CUDA available: {torch.cuda.is_available()}")
# If GPU is available, show which GPU is being used
if torch.cuda.is_available():
    st.sidebar.write(f"GPU: {torch.cuda.get_device_name(0)}")

# Define a function to load the Stable Diffusion model
# @st.cache_resource decorator caches the model to avoid reloading it on every run
@st.cache_resource
def load_model():
    try:
        # Inform user that model is loading
        st.write("Loading the model... This may take a few minutes on first run.")
        # Specify which Stable Diffusion model to use
        model_id = "runwayml/stable-diffusion-v1-5"
        # Determine whether to use GPU or CPU
        device = "cuda" if torch.cuda.is_available() else "cpu"
        st.write(f"Using device: {device}")
        
        # Load the model with appropriate settings
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            # Use float16 for GPU (faster) or float32 for CPU
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        # Move the model to the appropriate device (GPU or CPU)
        pipe = pipe.to(device)
        st.write("Model loaded successfully!")
        return pipe
    except Exception as e:
        # Show error message if model loading fails
        st.error(f"Error loading model: {str(e)}")
        return None

# Create a directory to store generated images if it doesn't exist
if not os.path.exists("generated_images"):
    os.makedirs("generated_images")

# Load the model
pipe = load_model()

# Stop the application if model loading failed
if pipe is None:
    st.error("Failed to load the model. Please check your internet connection and try again.")
    st.stop()

# Create the input form for user interaction
with st.form("image_generation_form"):
    # Text area for the main prompt
    prompt = st.text_area(
        "Enter your prompt:", 
        placeholder="A beautiful sunset over mountains, digital art, highly detailed, 4k, professional photography"
    )
    # Optional text area for negative prompt (what to avoid in the image)
    negative_prompt = st.text_area(
        "Negative prompt (optional):", 
        placeholder="blurry, low quality, distorted, bad anatomy, bad proportions, duplicate, watermark, signature"
    )
    
    # Advanced settings in an expander
    with st.expander("Advanced Settings"):
        # Slider to choose how many images to generate (1-4)
        num_images = st.slider("Number of images to generate", 1, 4, 1)
        
        # Image size selection
        image_size = st.selectbox(
            "Image Size",
            options=["512x512", "768x768", "1024x1024"],
            index=0
        )
        width, height = map(int, image_size.split('x'))
        
        # Quality settings
        guidance_scale = st.slider(
            "Guidance Scale (how closely to follow the prompt)",
            min_value=5.0,
            max_value=20.0,
            value=7.5,
            step=0.5
        )
        
        num_inference_steps = st.slider(
            "Number of Steps (higher = better quality but slower)",
            min_value=20,
            max_value=100,
            value=50,
            step=5
        )
        
        # Style modifiers
        style = st.selectbox(
            "Style",
            options=["None", "Photographic", "Digital Art", "Oil Painting", "Watercolor", "Anime"],
            index=0
        )
        
        # Add style-specific prompts
        style_prompts = {
            "None": "",
            "Photographic": "professional photography, 8k uhd, dslr, high quality, film grain, Fujifilm XT3",
            "Digital Art": "digital art, concept art, trending on artstation, highly detailed",
            "Oil Painting": "oil painting, masterpiece, detailed brushwork, rich colors",
            "Watercolor": "watercolor painting, soft edges, delicate colors, artistic",
            "Anime": "anime style, vibrant colors, cel shading, detailed background"
        }
        
        # Add style to prompt if selected
        if style != "None":
            prompt = f"{prompt}, {style_prompts[style]}"
    
    # Submit button
    submit = st.form_submit_button("Generate Image")

# Process the form submission
if submit and prompt:
    # Create a progress bar
    progress_bar = st.progress(0)
    # Create a placeholder for status messages
    status_text = st.empty()
    
    try:
        # Update status and progress
        status_text.text("Starting image generation...")
        progress_bar.progress(10)
        
        # Generate images
        status_text.text("Generating images... This may take a few minutes.")
        start_time = time.time()  # Start timing
        
        # Call the model to generate images
        images = pipe(
            prompt=prompt,  # Main prompt
            negative_prompt=negative_prompt if negative_prompt else None,  # Optional negative prompt
            num_images_per_prompt=num_images,  # Number of images to generate
            width=width,  # Image width
            height=height,  # Image height
            guidance_scale=guidance_scale,  # How closely to follow the prompt
            num_inference_steps=num_inference_steps  # Number of denoising steps
        ).images
        
        # Calculate and display generation time
        end_time = time.time()
        generation_time = end_time - start_time
        status_text.text(f"Generation completed in {generation_time:.2f} seconds!")
        progress_bar.progress(100)

        # Display and save each generated image
        for i, image in enumerate(images):
            # Show the image
            st.image(image, caption=f"Generated Image {i+1}")
            # Save the image to disk
            image_path = f"generated_images/image_{i+1}.png"
            image.save(image_path)
            # Create a download button for the image
            st.download_button(
                label=f"Download Image {i+1}",
                data=open(image_path, "rb").read(),
                file_name=f"generated_image_{i+1}.png",
                mime="image/png"
            )
    except Exception as e:
        # Show error message if generation fails
        st.error(f"An error occurred during image generation: {str(e)}")
        progress_bar.progress(0)
        status_text.text("Generation failed. Please try again.")

# Add helpful tips in the sidebar
st.sidebar.title("Tips for Better Results")
st.sidebar.write("""
### Prompt Writing Tips:
- Be specific and detailed
- Use descriptive adjectives
- Mention the style you want
- Include quality terms (e.g., "highly detailed", "4k")
- Add lighting conditions (e.g., "dramatic lighting", "soft lighting")

### Advanced Settings:
- Higher Guidance Scale (7-12) = More prompt adherence
- More Steps (50-75) = Better quality but slower
- Larger Image Size = More detail but slower generation

### Common Negative Prompts:
- blurry, low quality, distorted
- bad anatomy, bad proportions
- duplicate, watermark, signature
- text, logo, watermark
- extra limbs, missing limbs
""") 
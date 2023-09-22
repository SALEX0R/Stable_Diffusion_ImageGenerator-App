import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from authtoken import auth_token
from diffusers import StableDiffusionPipeline

# Create the main application window
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Dude")
ctk.set_appearance_mode("dark")

# Create the input prompt
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Futura", 20), text_color="ghost white", fg_color="MistyRose4")
prompt.place(x=10, y=10)

# Create the image display label
lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10, y=110)

# Model and device configuration
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"  # Use CPU if you don't have cuda or nvidia.
pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=auth_token)
pipe = pipe.to(device)

# Define the image generation function
def Generate():
    image = pipe(prompt.get(), guidance_scale=8.5)["Sample"][0]

    image.save('GeneratedImg.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

# Create the Generate button
trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Futura", 20), text_color="ghost white", fg_color="DeepSkyBlue4", command=Generate)
trigger.configure(text="Generate")
trigger.place(x=206, y=60)

# Start the main application loop
app.mainloop()

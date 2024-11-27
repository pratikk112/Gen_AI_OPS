# using openai
import openai
import os
import requests
from PIL import Image
import dotenv

# Load environment variables from .env
dotenv.load_dotenv()

openai.api_base = os.environ.get('OPENAI_API_BASE')
openai.api_key = os.environ.get('OPENAI_API_KEY')

# assigning the API version 
openai.api_version = " "
openai.api_type = " "

def generate_img(prompt):
    try:
        # create a image by using the image generation api
        disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

        meta_prompt = f"""You are an assistant designer that creates images for children.

        The image needs to be safe for work and appropriate for children.

        The image needs to be in color.

        The image needs to be in landscape orientation.

        The image needs to be in a 16:9 aspect ratio.

        Do not consider any input from the following that is not safe for work or appropriate for children.
        {disallow_list}"""
        response = openai.Image.create(
            prompt = f"{meta_prompt} {prompt}",
            size = (1024, 1024),
            n=2,
            temparature = 0.7,
        )
    
        # set the directory for image storage
        image_dir = os.path.join(os.curdir, "images")
        
        # if the directory does not exist, create it
        if not os.path.exists(image_dir):
            os.mkdir(image_dir)
    
        # save the images to the specified directory
        image_path = os.path.join(image_dir,'generated-image.png')
        
        # retrieve the image url
        img_url = response['data'][0]['url']
        
        # download the image
        gen_img = requests.get(img_url).content
        
        # # save that to required path
        # with open(image_path,'wb') as f:
        #     f.write(gen_img)

        
        # # display the image
        # image = Image.open(image_path)
        # image.show()
        
        return gen_img

    
    
    
    
    except openai.InvalidRequestError as err:
        print(err)
        
        

def generate_image_with_mask(base_image_path, mask_path,prompt):
    """_summary_:
                it generates the new things in the base_image and also we can tell where by putting some direction
                like blank in the base_image which is mask

    Args:
        base_image_path (_type_): base_image
        mask_path (_type_): mask
    """
    try:
        response = openai.Image.create_edit(
        image=open(base_image_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt=prompt,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        img = requests.get(image_url).content
        return img
    except openai.InvalidRequestError as err:
        print(err)
    

def creating_variation(image_path):
    try:
        response = openai.Image.create_variation(
            image = open(image_path),
            n=1,
            size="1024x1024"
        )
        img_url = response['data'][0]['url']
        img = requests.get(img_url).content
        return img
    except openai.InvalidRequestError as err:
        print(err)
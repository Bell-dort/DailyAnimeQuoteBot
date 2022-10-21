import random

from bing_image_downloader import downloader
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageOps, ImageFilter


class Tweet:
    def __init__(self, tweet_row):
        self.tweet_row = tweet_row
        self.quote = None
        self.image = None
        self.author = None
        self.anime = None

    def load(self):
        self.quote = self.tweet_row[0]
        self.author = self.tweet_row[1]
        self.anime = self.tweet_row[2]
        self.get_bckg_img()

    def get_bckg_img(self):
        imageString = "anime " + self.anime + " " + self.author
        downloader.download(imageString, limit=5, output_dir='dataset', adult_filter_off=False, force_replace=False,
                            timeout=10, verbose=True)
        imageNumber = random.randint(1, 5)

        try:
            self.image = Image.open('dataset/' + imageString + '/Image_' + str(imageNumber) + '.jpg')
        except:
            try:
                self.image = Image.open('dataset/' + imageString + '/Image_' + str(imageNumber) + '.png')
            except:
                try:
                    self.image = Image.open('dataset/' + imageString + '/Image_' + str(imageNumber) + '.jpeg')
                except:
                    print("Error no image found")
        image_box = self.image.getbbox()
        image_width = image_box[2]
        image_height = image_box[3]
        diff_size = abs(image_width - image_height)/2
        if image_width < image_height:
            self.image = self.image.crop((0, diff_size, image_width, image_width + diff_size))
        else:
            self.image = self.image.crop((diff_size, 0, image_height + diff_size, image_height))

        color_enhancer = ImageEnhance.Color(self.image)
        self.image = color_enhancer.enhance(2)

        brightness_enhancer = ImageEnhance.Brightness(self.image)
        self.image = brightness_enhancer.enhance(0.3)

        image_filter = ImageFilter.GaussianBlur(2)
        #self.image = self.image.filter(image_filter)
        font = ImageFont.truetype("Rochester-Regular.ttf", size=int(self.image.width/20))
        draw = ImageDraw.Draw(self.image)
        draw.text((self.image.width/2, self.image.width - self.image.width/10), '"' + self.quote + '"', font=font, anchor='mm')
        self.image.show()

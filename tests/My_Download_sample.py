"""

  2021/10/8 RaijinCheng
    * You have to download chromedriver.exe into your host (https://chromedriver.chromium.org/), specify the chromedriver path
    * The following is the example how you to download "塑膠飲料杯" for 1000 images, more argment please refer docs/arguments.rst

"""
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"塑膠飲料杯","limit":1000,"print_urls":True, "chromedriver":"D:\\AI_Garbage\\Bin\\chromedriver.exe", "format":"jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
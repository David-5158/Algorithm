# pip install git+https://github.com/Joeclienton1/google-images-download.git

from google_images_download import google_images_download

def googleImageCrawling(keyword, limit):
    response = google_images_download.googleimagesdownload()
 
    arguments = {"keywords":keyword,
                 "limit":limit,            # 크롤링 이미지 수
                 "print_urls":True,       # 이미지 url 출력
                 "chromedriver":"./chromedriver", "format": "jpg"
                 }  # 크롤링 이미지를 저장할 폴더
 
    paths = response.download(arguments)
    print(paths)
 
googleImageCrawling("Mom's illustration",10)
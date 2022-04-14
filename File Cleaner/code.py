import os
#os.path.dirname(os.path.abspath(__file__))
os.chdir("C:\\Users\\Arnab\\Desktop\\python proj")
l=os.listdir()

def folder(a):
    if not(os.path.exists(a)):
        os.makedirs(a)        

def move(a,b):
    for i in a:
        os.rename(i,f'{b}/{i}')

img=[".jpg",".jpeg",".gif",".png"]
doc=[".doc",".docx",".pdf",".ppt","pptx",".txt",".xlsx"]
media=[".mp3",".mp4","aac",".mov",".mvi"]
pro=[".c",".java",".exe",".py",".cpp"]
other=[".zip"]
print("-----Process is running------")
folder("image")
folder("docs")
folder("media")
folder("programs")
folder("other")
images=[item for item in l if os.path.splitext(item)[1].lower() in img]
documents=[item for item in l if os.path.splitext(item)[1].lower() in doc]
medias=[item for item in l if os.path.splitext(item)[1].lower() in media]
programs=[item for item in l if os.path.splitext(item)[1].lower() in pro]
others=[item for item in l if os.path.splitext(item)[1].lower() in other]
move(images,"image")
move(documents,"docs")
move(medias,"media")
move(programs,"programs")
move(others,"other")
print("-----Done------")



        
               
    

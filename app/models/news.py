class News:
    def __init__(self,name,id,linkurl,des,category):
        self.name=name
        self.id=id
        self.linkurl=linkurl
        self.des=des
        self.category = category

class Article:
    def __init__(self,id,nameheadline,image,link,timepublished,description):
        self.id=id
        self.nameheadline=nameheadline
        self.image=image
        self.link=link
        self.timepublished=timepublished
        self.description=description

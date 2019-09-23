# coding=UTF-8
import os
import shutil
import operator
import cv2
#1.找到外部文件夹
#2.计算图片数量
#3.顺序命名，封装成函数来调用 输入图片路径
def get_all_files(bg_path):
    files = []

    for f in os.listdir(bg_path):
        if os.path.isfile(os.path.join(bg_path, f)):
            files.append(os.path.join(bg_path, f))
        else:
            files.extend(get_all_files(os.path.join(bg_path, f)))
    files.sort(key=lambda x: int(x[-9:-4]))#排序从小到大
    return files
path=["./OcclusionChallengeICCV2015"]

outpath='./outdatatest/'
img_path="./OcclusionChallengeICCV2015/image"
xml_path="./OcclusionChallengeICCV2015/xml"

temp=0
if os.path.exists(img_path) and os.path.exists(xml_path):
    num_img=get_all_files(img_path)
    xml_img=get_all_files(xml_path)
else:
    exit("no more")
for i in range(len(xml_img)):
    if operator.eq(xml_img[i][-9:-4],num_img[i][-9:-4]):

        name = '%06d' % int(temp)
        pic_name=outpath+'ImageSets/'+name+'.jpg'

            #png转jpg
        p=cv2.imread(num_img[i])
        cv2.imwrite(pic_name,p)
       
        xml_name=outpath+'Annotations/'+name+'.xml'

        shutil.copy(xml_img[i],xml_name)
        temp+=1

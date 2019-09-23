# coding=UTF-8
import os
import shutil
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
path=["./output1","./output2","./output3","./output4","./output5","./output6","./output7","./output8","./output9","./output10","./output11","./output12","./output13"]
categorys_all = ['ape','can','cat','driller','duck','eggbox','glue','holepuncher']
outpath='../outdata/'
name_flag=0
for i in path:
    for t in categorys_all:
        img_path=i+"/"+t+"/image"
        xml_path=i+"/"+t+"/xml"

        temp=name_flag
        if os.path.exists(img_path) and os.path.exists(xml_path):
            num_img=get_all_files(img_path)
            xml_img=get_all_files(xml_path)
        else:
            continue
        if cmp(num_img,xml_img):
            for t in num_img:
                name = '%06d' % int(temp)
                pic_name=outpath+'image/'+name+'.jpg'
                print(t)
                shutil.copy(t,pic_name)
                temp+=1

            temp=name_flag
            
            
            for z in xml_img:
                name = '%06d' % int(temp)
                xml_name=outpath+'xml/'+name+'.xml'
                print(z)
                shutil.copy(z,xml_name)
                temp+=1
            name_flag=temp

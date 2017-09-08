# encoding: utf-8
import numpy as np
import numpy
import cv2
import sys
import collections
from matplotlib import gridspec
from matplotlib.font_manager import FontProperties
import matplotlib
matplotlib.use('Qt4Agg')

reload(sys)
sys.setdefaultencoding("utf-8")
class Image:
    '''
        如果type=url
        getimg參數要傳入requests回傳的content
        如果type=local
        getimg參數要傳入圖片本地路徑
        '''

    def __init__(self, getimg, type='url'):
        #  設置 matplotlib 中文字體
        self.font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
        #  儲存檔名
        # self.imageName = ImgName
        # #  儲存路徑
        # self.Path = Path
        #  用來儲放分割後的圖片邊緣坐標(x,y,w,h)
        self.arr = []
        #  將每個階段做的圖存起來 用來debug
        self.dicImg = collections.OrderedDict()
        #  將圖片做灰階
        # self.im = cv2.imread(Path + "\\" + ImgName)
        if type == 'url':
            image = np.asarray(bytearray(getimg), dtype="uint8")
            self.im = cv2.imdecode(image, cv2.IMREAD_COLOR)
        elif type == 'local':
            self.im = cv2.imread(getimg)



if __name__ == '__main__':
    path = r'D:\FailCaptcha\26.png'
    x = Image(path,'local')


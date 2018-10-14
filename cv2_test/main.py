import cv2

def on_mouse(event, x, y, flags, param):
    global point_start, point_end
    # 双击
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
    # 按下
    if event == cv2.EVENT_LBUTTONDOWN:
        point_start =  (x, y)
        print('按下')
    # 松开
    if event == cv2.EVENT_LBUTTONUP:
        point_end = (x,y)
        print('松开',point_start,point_end)
        cv2.rectangle(img, point_start,point_end,(0,255,0),2)
        cv2.imshow('Image',img)

img_path = '/home/fc/Downloads/test.jpg'
img = cv2.imread(img_path)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image',on_mouse)
cv2.imshow('Image',img)
cv2.waitKey(0)

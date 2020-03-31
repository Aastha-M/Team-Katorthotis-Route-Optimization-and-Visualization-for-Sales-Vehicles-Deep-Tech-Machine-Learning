import cv2
def draw_junctions(jc,img):
    c=(0,0,0)
    r=20
    font = cv2.FONT_HERSHEY_SIMPLEX
    jno=1
    for cc in jc:
        img=cv2.circle(img,cc,r,c,-1)
        tc=(int(cc[0]-r/2-8),int(cc[1]+r/2))
        img=cv2.putText(img, 'J'+str(jno), tc, font,  1, (255,255,255), 2, cv2.LINE_AA)
        jno+=1
    return(img)
img_org=cv2.imread(r'C:\Users\Abi\Documents\academics\projects\sales_vehicle\vizualization\map.png')
jc=[(832,87),(685,204),(301,548),(41,733),(739,689),(1242,637)]
img=draw_junctions(jc,img_org)
cv2.imshow('map',img)
cv2.imwrite('map_junc.png',img)
'''cc=(832,87)

c=(0,0,0)
r=20
font = cv2.FONT_HERSHEY_SIMPLEX
tc=(int(cc[0]-r/2-5),int(cc[1]+r/2))
img=cv2.circle(img_org,cc,r,c,-1)
img=cv2.putText(img, 'J1', tc, font,  1, (255,255,255), 2, cv2.LINE_AA) 
cv2.imshow('map',img)'''

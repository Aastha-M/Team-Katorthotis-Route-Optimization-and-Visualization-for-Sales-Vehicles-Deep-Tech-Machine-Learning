import cv2
import math
import time
def draw_junctions(jc,img,co=(0,0,0),jno=1):
    c=co
    r=20
    font = cv2.FONT_HERSHEY_SIMPLEX
    #jno=1
    for cc in jc:
        img=cv2.circle(img,cc,r,c,-1)
        tc=(int(cc[0]-r/2-8),int(cc[1]+r/2))
        img=cv2.putText(img, 'J'+str(jno), tc, font,  1, (255,255,255), 2, cv2.LINE_AA)
        jno+=1
    return(img)
def draw_veh(cc,img):
    r=20
    font = cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.circle(img,cc,r,(0,0,255),-1)
    return(img)
def disp_game(img,pos_log):
    for i in pos_log:
        img2=img.copy()
        img2=draw_veh(i,img2)
        bg_rs=cv2.resize(img2,(500,500),interpolation = cv2.INTER_AREA)
        cv2.imshow('game',bg_rs)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.01)
    time.sleep(1)
    cv2.destroyAllWindows()

        
def game_replay(fn):
    speed=5
    img=cv2.imread('map_junc.png')
    jc=[(832,87),(685,204),(301,548),(41,733),(739,689),(1242,637)]
    f=open(fn,'r')
    s=f.read()
    lines=s.split('\n')
    st=lines[0]
    st=st.split(',')
    sourc=int(st[0])
    dest=int(st[1])
    ##generating map
    sj=jc[sourc]
    tj=jc[dest]
    img=draw_junctions([sj],img,(0,0,255),sourc+1)
    img=draw_junctions([tj],img,(0,255,0),dest+1)
    pos=sj
    pos_log=[pos,pos,pos,pos,pos,pos,pos,pos,pos,pos,pos,pos,pos,pos,pos,pos]
    for i in range(1,len(lines)-1):
        trg=jc[int(lines[i])]
        l1=min(pos[0],trg[0])
        l2=min(pos[1],trg[1])
        u1=max(pos[0],trg[0])
        u2=max(pos[1],trg[1])
        h=u2-l2
        b=u1-l1
        xs=math.copysign(1,trg[0]-pos[0])
        ys=math.copysign(1,trg[1]-pos[1])
        b=max(b,0.00000000000001)
        theta=math.atan(h/b)
        dx=math.cos(theta)*speed*xs
        dy=math.sin(theta)*speed*ys
        #print('pos:')
        #print(pos)
        #print('trg:')
        #print(trg)
        #print('dx and dy:')
        #print(dx)
        #print(dy)
        while(1):
            pos=(pos[0]+dx,pos[1]+dy)
            pos_int=(int(pos[0]),int(pos[1]))
            pos_log.append(pos_int)
            x2t=(trg[0]-pos[0])*xs
            y2t=(trg[1]-pos[1])*ys
            #print('pos:'+str(pos))
            #print('x2t:'+str(x2t))
            #print('y2t:'+str(y2t))
            if(x2t<0 and y2t<0):
                break
    #print(pos_log)
    disp_game(img,pos_log)
        
fn=r'test.txt'
game_replay(fn)

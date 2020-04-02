#stage 1
#list of distribution point
distp=input('Enter list of distribution points')
distll=[[13.073797, 77.530916],[12.901046, 77.488457],[12.994069, 77.555465],[12.908283, 77.503177],[13.067845, 77.532842]]
#[[12.993597, 77.554774],[13.073797, 77.530916],[12.901046, 77.488457],[12.994078, 77.555242],[12.993738, 77.555437]]
#list(map(int,input("\nEnter latitude and longitude of distribution points: ").strip().split())) 
#list of delivery points
delvp=input('Enter list of delivery points')
delpll=[[12.994078, 77.555242],[13.072350, 77.528185],[12.993680, 77.555002],[12.993597, 77.554774],[12.993738, 77.555437]]
#[[12.993680, 77.555002],[13.067845, 77.532842],[12.994069, 77.555465],[13.072350, 77.528185],[12.908283, 77.503177]]
#list(map(int,input("\nEnter latitude and longitude of delivery points: ").strip().split())) 
i=0
j=0
k=[]
b=[]
#using the parameter of most nearby distribution point a suitable distribution point is assigned to each deilvery point
#calculation of shortest distance
for x in delpll:
	for y in distll:
		lat=x[0]-y[0]
		lon=x[1]-y[1]
		dist=((lat**2)+(lon**2))**0.5
		b.append(dist)
		i=i+1
	minpos=b.index(min(b))
	k.append(minpos)
	j=j+1
	b=[]
	i=0
#list of distribution point assigned to each delivery point in order
print(k)


#stage 2
ba=[[13.073797, 77.530916],[12.901046, 77.488457],[13.072350, 77.528185],[13.067845, 77.532842],[12.908283, 77.503177]]
ab=[[12.993680, 77.555002],[12.993738, 77.555437],[12.994069, 77.555465],[12.994078, 77.555242],[12.993597, 77.554774]]
#vehicletype=[truck,cab,motorbike]
vehicell=[ab,ba,ab,ba,ab]
ii=0
jj=0
kk=[]
bb=[]
#using the parameter of most nearby vehicle a suitable vehicle is assigned to each ditribution point
#calculation of shortest distance
for xx in k:
	dist1=distll[xx]
	veh=vehicell[xx]
	for yy in veh:
		latt=dist1[0]-yy[0]
		lonn=dist1[1]-yy[1]
		distt=((latt**2)+(lonn**2))**0.5
		bb.append(distt)
		ii=ii+1
	minposs=bb.index(min(bb))
	kk.append(minposs)
	jj=jj+1
	bb=[]
	ii=0
#list of vehicles for each distribution point in order
print(kk)

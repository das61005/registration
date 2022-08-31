import copy
import numpy as np
import open3d as o3
from probreg import cpd
import time


def prn_obj(obj): 
    print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

# load source and target point cloud
source = o3.geometry.PointCloud()
target = o3.geometry.PointCloud()
source.points = o3.utility.Vector3dVector(np.loadtxt("before_mask.txt"))
target.points = o3.utility.Vector3dVector(np.loadtxt("after_mask.txt"))
print(source)
print(target)

# compute cpd registration
start = time.time()
tf_param, _, _ = cpd.registration_cpd(source, target)
result = copy.deepcopy(source)
result.points = tf_param.transform(result.points)
elapsed = time.time() - start
print("time: ", elapsed)
prn_obj(tf_param)

transform_matrix_rot=open('transform_matrix_rot.txt','w')
for rot in tf_param.rot:
    transform_matrix_rot.write(str(rot[0])+' '+str(rot[1])+' '+str(rot[2])+'\n')

transform_matrix_t=open('transform_matrix_t.txt','w')
transform_matrix_t.write(str(tf_param.t[0])+' '+str(tf_param.t[1])+' '+str(tf_param.t[2])+'\n')

scale_txt=open('scale.txt','w')
scale_txt.write(str(tf_param.scale))

# draw result
source.paint_uniform_color([1, 0, 0])
target.paint_uniform_color([0, 1, 0])
result.paint_uniform_color([0, 0, 1])
#o3.visualization.draw_geometries([ target, result])
#############################################################
before_txt=np.loadtxt('before_mask.txt')
after_txt=np.loadtxt('after_mask.txt')
tranform_matrix=tf_param.rot
tranform_matrix2=tf_param.t
scale=tf_param.scale


tranform_mask_txt=before_txt#+target.get_center()-source.get_center()
tranform_mask= o3.geometry.PointCloud()
tranform_mask.points=o3.utility.Vector3dVector(tranform_mask_txt)
tranform_mask.paint_uniform_color([ 0.706, 0,0 ])
tranform_mask=tranform_mask.translate(target.get_center(), relative=False)
tranform_mask=tranform_mask.scale(scale,source.get_center())
tranform_mask=tranform_mask.rotate(tranform_matrix)#,center=after_mask.get_center()
    


o3.visualization.draw_geometries([ source,target,result])#,tranform_mask



import open3d as o3d
import numpy as np
from scipy.spatial.transform import Rotation

before_txt=np.loadtxt('before_mask.txt')
after_txt=np.loadtxt('after_mask.txt')
tranform_matrix=np.loadtxt('transform_matrix_rot.txt')
tranform_matrix2=np.loadtxt('transform_matrix_t.txt')
scale=np.loadtxt('scale.txt')#same_rotate/

##對照befor_mask ,after_mask ,predict_mask
before_mask = o3d.geometry.PointCloud()
before_mask.points = o3d.utility.Vector3dVector(before_txt)
before_mask.paint_uniform_color([1, 0, 0])

after_mask = o3d.geometry.PointCloud()
after_mask.points = o3d.utility.Vector3dVector(after_txt)
after_mask.paint_uniform_color([0, 1, 0])


tranform_mask_txt=before_txt#+after_mask.get_center()-before_mask.get_center()#+after_mask.get_center()-before_mask.get_center()#
tranform_mask= o3d.geometry.PointCloud()
tranform_mask.points=o3d.utility.Vector3dVector(tranform_mask_txt)
tranform_mask.paint_uniform_color([ 0, 0, 0.706])
tranform_mask=tranform_mask.rotate(tranform_matrix)#,center=after_mask.get_center()
tranform_mask=tranform_mask.scale(scale,after_mask.get_center())
tranform_mask=tranform_mask.translate(after_mask.get_center(), relative=False)#



o3d.visualization.draw_geometries([before_mask,tranform_mask,after_mask])

#給befoe_mask中的點來映射到after_mask上
print("before",before_txt)#before_txt
before=before_txt#before_txt[219,227,79]
after=(np.dot(before,tranform_matrix.T)+tranform_matrix2)*scale
after=[[round(i[0]),round(i[1]), round(i[2])] for i in after]
after=np.array(after)
print("after",after)

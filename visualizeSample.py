import numpy as np
import open3d as o3d

# 读取npz文件
data = np.load('data/SdfSamples/Vertebrae/03001627/Object_7.npz')


# 提取pos和neg数据
pos_data = data['pos']  # 假设正值数据存储在'pos'数组中
neg_data = data['neg']  # 假设负值数据存储在'neg'数组中

# 合并数据
points = np.vstack((pos_data, neg_data))

# 打印总共的点数
total_points = points.shape[0]
print(f"总共点数: {total_points}")

# 根据SDF值设置颜色
colors = np.array([[1, 0, 0] if sdf > 0 else [0, 1, 0] if sdf == 0 else [0, 0, 1] for sdf in points[:, 3]])

# 创建Open3D点云对象
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points[:, :3])
point_cloud.colors = o3d.utility.Vector3dVector(colors)

# 可视化点云
o3d.visualization.draw_geometries([point_cloud])

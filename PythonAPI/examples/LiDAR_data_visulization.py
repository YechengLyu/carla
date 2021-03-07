#%%
import numpy as np
import open3d as o3d
from plyfile import PlyData, PlyElement

LABEL_COLORS = np.array([
    (255, 255, 255), # None
    (70, 70, 70),    # Building
    (100, 40, 40),   # Fences
    (55, 90, 80),    # Other
    (220, 20, 60),   # Pedestrian
    (153, 153, 153), # Pole
    (157, 234, 50),  # RoadLines
    (128, 64, 128),  # Road
    (244, 35, 232),  # Sidewalk
    (107, 142, 35),  # Vegetation
    (0, 0, 142),     # Vehicle
    (102, 102, 156), # Wall
    (220, 220, 0),   # TrafficSign
    (70, 130, 180),  # Sky
    (81, 0, 81),     # Ground
    (150, 100, 100), # Bridge
    (230, 150, 140), # RailTrack
    (180, 165, 180), # GuardRail
    (250, 170, 30),  # TrafficLight
    (110, 190, 160), # Static
    (170, 120, 50),  # Dynamic
    (45, 60, 150),   # Water
    (145, 170, 100), # Terrain
]) / 255.0 # normalize each channel [0-1] since is what Open3D uses




#%%
data = PlyData.read("_out/00000001.ply")
xyz = np.vstack((data.elements[0].data['x'],data.elements[0].data['y'],data.elements[0].data['z'])).T

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)

sem_label =  data.elements[0].data['ObjTag']
int_color = LABEL_COLORS[sem_label]

point_list = o3d.geometry.PointCloud()
point_list.points = o3d.utility.Vector3dVector(xyz) 
point_list.colors = o3d.utility.Vector3dVector(int_color)
o3d.visualization.draw_geometries([point_list])
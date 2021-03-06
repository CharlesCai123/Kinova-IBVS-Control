import numpy as np

# def getIM(s:np.ndarray, z):
#     u, v = s
#     IM = np.array([[-f/z, 0, u/z, u*v/f, -(f**2 + u**2)/f, v],
#                    [0, -f/z, v/z, (f**2 + v**2)/f, -u*v/f, -u]])
#     return IM

'''
[u v]' = Mat_intrinsics @ [Xc Yc Zc]'
[u v]' = Mat_intrinsics_ @ [Xc_ Yc_ Zc_]'
Mat_intrinsics @ [Xc Yc Zc]' = Mat_intrinsics_ @ [Xc_ Yc_ Zc_]'
'''
Mat_intrinsics = np.array([[640, 0], [0, 480]]) @ np.array([[1.11111, 0, 0.5],
                                                            [0, 1.48148, 0.5]])
Mat_intrinsics = np.array([[2064, 0], [0, 2096]]) @ np.array([[1.0941 / 2, 0, 0.5],
                                                              [0, 1.1111 / 2, 0.5]])

fx = Mat_intrinsics[0][0]
fy = Mat_intrinsics[1][1]
cx = Mat_intrinsics[0][2]
cy = Mat_intrinsics[1][2]

'''
Get Interaction Matrix
'''


# global fx, fy, cx, cy


def getIM(s: np.ndarray, z) -> np.ndarray:
    x, y = s
    IM = np.array(
        [[(x - cx) * (y - cy) / fy, -(fx ** 2 + (x - cx) ** 2) / fx, (y - cy) * fx / fy, -fx / z, 0, (x - cx) / z],
         [(fy ** 2 + (y - cy) ** 2) / fy, -(x - cx) * (y - cy) / fx, -(x - cx) * fy / fx, 0, -fy / z, (y - cy) / z]])
    return IM

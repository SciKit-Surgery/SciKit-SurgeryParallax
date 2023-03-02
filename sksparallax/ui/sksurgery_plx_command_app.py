# coding=utf-8

""" Demo app, to show OpenCV video and PySide2 widgets together."""

import sys
from PySide2.QtWidgets import QApplication
import numpy
from PySide2.QtWidgets import QApplication
from sksurgeryutils.common_overlay_apps import OverlayBaseWidget
from sksurgerycore.transforms.transform_manager import TransformManager
from sksurgeryarucotracker.arucotracker import ArUcoTracker
from sksurgeryvtk.models.vtk_cylinder_model import VTKCylinderModel
from sksurgeryvtk.utils.matrix_utils import create_vtk_matrix_from_numpy

from sksparallax.parallax_widget import ParallaxWidget

def run(calib_dir, model_dir, focal_distance, camera_pos, 
        scale_motion, show_cross_hairs, video_source, aruco_source):

    """ Prints command line args, and launches main screen."""

    app = QApplication([])

    viewer = ParallaxWidget(video_source, init_widget = False, 
            aruco_source = aruco_source, focal_point = focal_distance, 
            scaling = scale_motion)

    viewer.add_vtk_models_from_dir(model_dir)

    x_axis = VTKCylinderModel(height = 200, radius = 3.0,
            colour = (0., 1., 0.), name = "x_axis",
            angle = 90.0, orientation = (0., 0., 1.))
    y_axis = VTKCylinderModel(height = 200, radius = 3.0,
            colour = (1., 0., 0.), name = "y_axis",
            angle = 0.0, orientation = (1., 0., 0.))
    z_axis = VTKCylinderModel(height = 200, radius = 3.0,
            colour = (0., 0., 1.), name = "z_axis",
            angle = 90.0, orientation = (1., 0., 0.))
    
    to_fp = numpy.eye(4)
    to_fp[2,3] = focal_distance
    y_axis.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))
    x_axis.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))
    z_axis.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))

    if show_cross_hairs:
        viewer.vtk_overlay_window.add_vtk_models([x_axis])
        viewer.vtk_overlay_window.add_vtk_models([y_axis])
        viewer.vtk_overlay_window.add_vtk_models([z_axis])

    viewer.show()
    viewer.vtk_overlay_window.Initialize()
    viewer.vtk_overlay_window.Start()
    viewer.start()
    camera=viewer.vtk_overlay_window.get_foreground_camera()
    camera.SetPosition(0., 0., camera_pos)
    current_pos=camera.GetPosition()
    print ('position=',current_pos)

    sys.exit(app.exec_())

    viewer.vtk_overlay_window.close()

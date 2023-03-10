# coding=utf-8

""" Demo app, to show OpenCV video and PySide2 widgets together."""

import sys
from PySide2.QtWidgets import QApplication
from sksurgeryutils.common_overlay_apps import OverlayBaseWidget
from sksurgerycore.transforms.transform_manager import TransformManager
from sksurgeryarucotracker.arucotracker import ArUcoTracker

from sksparallax.parallax_widget import ParallaxWidget
from sksparallax.geometry import add_crosshairs, add_cube_grid

def run(calib_dir, model_dir, focal_distance, camera_pos, 
        scale_motion, show_cross_hairs, show_cube, video_source, 
        aruco_source):

    """ Prints command line args, and launches main screen."""

    app = QApplication([])

    viewer = ParallaxWidget(video_source, init_widget = False, 
            aruco_source = aruco_source, focal_point = focal_distance, 
            scaling = scale_motion)

    viewer.add_vtk_models_from_dir(model_dir)

    if show_cross_hairs:
        add_crosshairs(viewer, focal_distance)
   
    if show_cube:
        add_cube_grid(viewer)

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

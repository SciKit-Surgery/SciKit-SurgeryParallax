# coding=utf-8

""" Command line processing for videolag app. """

import argparse
from sksparallax.ui.sksurgery_plx_command_app import run


def main(args=None):
    """Entry point for sksurgeryparallax application"""

    parser = argparse.ArgumentParser(description='sksurgeryplx')


    parser.add_argument("-k", "--calib_dir",
                        required=False,
                        type=str,
                        help="Directory containing calibration data.")
   
    parser.add_argument("-m", "--model_dir",
                        required=False,
                        type=str,
                        default="./models",
                        help="Directory containing model data.")
   
    parser.add_argument("-f", "--focal_point",
                        required=False,
                        type=float,
                        default=100,
                        help="The z location of the camera focal point")

    parser.add_argument("-c", "--camera_position",
                        required=False,
                        type=float,
                        default=-500,
                        help="The z location of the camera position")
   
    parser.add_argument("-s", "--scale_motion",
                        required=False,
                        type=float,
                        default=0.5,
                        help="Scale the camera motion by this amount")

    parser.add_argument("-x", "--show_crosshairs", action='store_true',
                        help="Show cross hairs representing the focal point")

    parser.add_argument("-g", "--show_grid", action='store_true',
                        help="Show a grid")

    parser.add_argument("-i", "--video_source",
                        required=False,
                        type=int,
                        default=0,
                        help="Source for the video image")

    parser.add_argument("-a", "--aruco_source",
                        required=False,
                        type=int,
                        default=1,
                        help="Source for the aruco tracker")

    parser.add_argument("-d", "--depth",
                        required=False,
                        type=int,
                        default=0,
                        help="Source for the video image")


    version_string = 'aplha'
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "-v", "--version",
        action='version',
        version='sksurgeryparallax version ' + friendly_version_string)

    args = parser.parse_args(args)

    run(args.calib_dir, args.model_dir, args.focal_point, args.camera_position,
            args.scale_motion, args.show_crosshairs, args.show_grid,
            args.video_source, args.aruco_source, args.depth)


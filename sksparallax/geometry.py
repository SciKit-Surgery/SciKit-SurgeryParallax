import numpy
from sksurgeryvtk.models.vtk_cylinder_model import VTKCylinderModel
from sksurgeryvtk.utils.matrix_utils import create_vtk_matrix_from_numpy

def add_crosshairs ( viewer, z_origin):
    """
    creates a cross hair model and adds it to the viewer
    """

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
    to_fp[2,3] = z_origin 
    y_axis.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))
    x_axis.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))
    z_axis.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))

    viewer.vtk_overlay_window.add_vtk_models([x_axis])
    viewer.vtk_overlay_window.add_vtk_models([y_axis])
    viewer.vtk_overlay_window.add_vtk_models([z_axis])



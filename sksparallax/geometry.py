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


def add_cube_grid ( viewer, spacing = 40, line_width = 0.2, cube_width = 160, 
        cube_height = 160, cube_depth = 160):
    """
    creates a 3D grid model and adds it to the viewer
    """

    #the x lines
    for z_pos in numpy.arange (- cube_depth/2., cube_depth/2. + 1, spacing):
        for y_pos in numpy.arange (- cube_height/2., cube_height/2. + 1, spacing):
            
            x_line = VTKCylinderModel(height = cube_width, radius = line_width,
                colour = (0.412, 0.412, 0.412), name = "x_axis",
                angle = 90.0, orientation = (0., 0., 1.))
    
            to_fp = numpy.eye(4)
            to_fp[1,3] = y_pos 
            to_fp[2,3] = z_pos 
            x_line.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))
            viewer.vtk_overlay_window.add_vtk_models([x_line])
    
    #the y_lines
    for z_pos in numpy.arange (- cube_depth/2., cube_depth/2. + 1 , spacing):
        for x_pos in numpy.arange (- cube_width/2., cube_width/2. + 1, spacing):
            
            y_line = VTKCylinderModel(height = cube_height, radius = line_width,
                colour = (0.412, 0.412, 0.412), name = "y_axis",
                angle = 0.0, orientation = (1., 0., 0.))
            
            to_fp = numpy.eye(4)
            to_fp[0,3] = x_pos 
            to_fp[2,3] = z_pos 
            y_line.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))
            viewer.vtk_overlay_window.add_vtk_models([y_line])
    
    #the z_lines
    for x_pos in numpy.arange (- cube_width/2., cube_width/2. + 1, spacing):
        for y_pos in numpy.arange (- cube_height/2., cube_height/2. + 1, spacing):
            
            x_line = VTKCylinderModel(height = cube_width, radius = line_width,
                colour = (0.412, 0.412, 0.412), name = "z_axis",
                angle = 90.0, orientation = (0., 0., 1.))
    
            z_line = VTKCylinderModel(height = cube_depth, radius = line_width,
                colour = (0., 0., 1.), name = "z_axis",
                angle = 90.0, orientation = (1., 0., 0.))
            
            to_fp = numpy.eye(4)
            to_fp[0,3] = x_pos 
            to_fp[1,3] = y_pos 
            z_line.set_user_matrix(create_vtk_matrix_from_numpy(to_fp))
            viewer.vtk_overlay_window.add_vtk_models([z_line])


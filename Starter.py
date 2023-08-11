import vtk

# Load the VTK data file
reader = vtk.vtkStructuredPointsReader()
reader.SetFileName("brain.vtk")
reader.Update()

# Get the scalar range of the data
scalar_range = reader.GetOutput().GetScalarRange()

#Creating a volume mapper as well as a volume property
vol_map = vtk.vtkSmartVolumeMapper()
vol_map.SetInputConnection(reader.GetOutputPort())
vol_prop = vtk.vtkVolumeProperty()
vol_prop.ShadeOff()

# Color map
color = vtk.vtkColorTransferFunction()
color.AddRGBPoint(scalar_range[0], 0.0, 0.0, 0.0)
color.AddRGBPoint(scalar_range[0]+50, 1.0, 1.0, 1.0)
color.AddRGBPoint(scalar_range[0]+75, 1.0, 1.0, 0.0)
color.AddRGBPoint(scalar_range[0]+100, 1.0, 0.0, 0.0)
color.AddRGBPoint(scalar_range[1], 1.0, 0.0, 0.0)

# Opacity
opacity = vtk.vtkPiecewiseFunction()
opacity.AddPoint(scalar_range[0], 0.0)
opacity.AddPoint(scalar_range[0]+50, 0.1)
opacity.AddPoint(scalar_range[0]+75, 0.2)
opacity.AddPoint(scalar_range[0]+100, 0.5)
opacity.AddPoint(scalar_range[1], 1.0)

# Setters
vol_prop.SetColor(color)
vol_prop.SetScalarOpacity(opacity)

#Volume
volume = vtk.vtkVolume()
volume.SetMapper(vol_map)
volume.SetProperty(vol_prop)


renderer = vtk.vtkRenderer()
renderer.AddVolume(volume)
rend_window = vtk.vtkRenderWindow()
rend_window.SetSize(800, 600)
rend_window.AddRenderer(renderer)

# Create an interactor and start the render loop
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(rend_window)
interactor.Initialize()
interactor.Start()

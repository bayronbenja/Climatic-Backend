import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.image as mpimg  # Para cargar la imagen
import matplotlib.ticker as mticker  # Para configurar los intervalos de la grilla

from cartopy.mpl.ticker import (LongitudeFormatter, LatitudeFormatter,
                                LatitudeLocator)
import xarray
import os


def contour_plot(variable, dataset, shading=True):
    """
    Grafica la temperatura sobre una imagen de fondo.

    - variable: Variable a graficar. 
      - Temperatura a 2 metros de la superficie: 't2m'
      - Temperatura (level): "t"
      - Temperatura en la superficie del mar: "sst"
      - Humedad específica: "q"
      - Radiación solar incidente: "tisr"

    Parameters:
    - dataset: Dataset con los datos de temperatura.
    - image_path: Ruta de la imagen a usar como fondo.
    - image_path: Ruta de la imagen a usar como fondo en contorno.
    - image_path2: Ruta de la imagen a usar para cubrir los bordes.
    - extent: Extensión geográfica de la imagen [min_lon, max_lon, min_lat, max_lat].
    - shading: Booleano para graficar el contorno o no.
    """
    image_path = os.getcwd()+"/image/Mapa_REGION_border-Photoroom.png"  # Reemplaza con la ruta de tu imagen
    image_path_C = os.getcwd()+'/image/MAPA_Comunas_sexta_region.png'  # Reemplaza con la ruta de tu imagen
    image_path2 = os.getcwd()+'/image/Region_FULL_FILL.png'  # Reemplaza con la ruta de tu imagen
    
    
    # Extraer datos del dataset
    temperature = dataset.values - 273.15  # Kelvin a Celsius

    if variable == "t2m" or variable == "t" or "sst":
      datos = dataset.values - 273.15  # Kelvin a Celsius
    elif variable == "q": # Por si se quisiera hacer un arreglo de unidad de medida
      datos = dataset.values
    elif variable == "tisr": # Por si se quisiera hacer un arreglo de unidad de medida
      datos = dataset.values

    lats = dataset['latitude'].values
    lons = dataset['longitude'].values

    date = str(dataset['time'].values)[:10]
    date_h = str(dataset['time'].values)[11:16]

    extent = [dataset['longitude'].values.min(),dataset['longitude'].values.max(),dataset['latitude'].values.min(),dataset['latitude'].values.max()]

    # Crear figura y ejes con Cartopy
    fig = plt.figure(figsize=(8, 6), dpi=150)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Cargar y mostrar la imagen de fondo
    img = mpimg.imread(image_path)
    ax.imshow(img, origin='upper', extent=extent, transform=ccrs.PlateCarree(), zorder=3)

    img2 = mpimg.imread(image_path2)
    ax.imshow(img2, origin='upper', extent=extent, transform=ccrs.PlateCarree(), zorder=5)

    # Graficar los datos
    if shading:
        cont = ax.contourf(
            lons, lats, datos, cmap='RdYlBu_r', transform=ccrs.PlateCarree(), levels=15,
            zorder=1
        )
    else:
      img = mpimg.imread(image_path_C)
      ax.imshow(img, origin='upper', extent=extent, transform=ccrs.PlateCarree(), zorder=3)
      cont = ax.contour(
          lons, lats, datos, cmap='RdYlBu_r', transform=ccrs.PlateCarree(), levels=20,
          zorder=4)
      ax.clabel(cont,
            inline=1,
            fontsize=8,
            fmt=' {:.0f} '.format,  # Labes as integers, with some extra space.
      # Cut the line where the label will be placed.
        )
    
    # Configurar el colorbar,  para que tenga más valores y se ajuste a la variable
    if variable == "t2m":
      cbar = plt.colorbar(cont, orientation='vertical', pad=0.15, fraction=0.03, label='Unidades (°C)')
      cbar.locator = mticker.MaxNLocator(nbins=20)  # Cambia el número de etiquetas
      cbar.update_ticks()  # Actualiza las etiquetas en el colorbar
      plt.title(f'Temperatura a 2 metros sobre la superficie\n{date} - {date_h}', size=10, weight='bold')

    elif variable == "t":
      cbar = plt.colorbar(cont, orientation='vertical', pad=0.15, fraction=0.03, label='Unidades (°C)')
      cbar.locator = mticker.MaxNLocator(nbins=20)  # Cambia el número de etiquetas
      cbar.update_ticks()  # Actualiza las etiquetas en el colorbar
      plt.title(f'Temperatura (level)\n{date} - {date_h}', size=10, weight='bold')

    elif variable == "sst":
      cbar = plt.colorbar(cont, orientation='vertical', pad=0.15, fraction=0.03, label='Unidades (°C)')
      cbar.locator = mticker.MaxNLocator(nbins=20)  # Cambia el número de etiquetas
      cbar.update_ticks()  # Actualiza las etiquetas en el colorbar
      plt.title(f'Temperatura en la superficie del mar\n{date} - {date_h}', size=10, weight='bold')

    elif variable == "q":
      cbar = plt.colorbar(cont, orientation='vertical', pad=0.15, fraction=0.03, label='Unidades (g/kg) (gramos por kilogramo)')
      cbar.locator = mticker.MaxNLocator(nbins=20)  # Cambia el número de etiquetas
      cbar.update_ticks()  # Actualiza las etiquetas en el colorbar
      plt.title(f'Humedad específica\n{date} - {date_h}', size=10, weight='bold')
      
    elif variable == "tisr":
      cbar = plt.colorbar(cont, orientation='vertical', pad=0.15, fraction=0.03, label='Unidades (W/m^2) (vatios por metro cuadrado)')
      cbar.locator = mticker.MaxNLocator(nbins=20)  # Cambia el número de etiquetas
      cbar.update_ticks()  # Actualiza las etiquetas en el colorbar
      plt.title(f'Radiación solar incidente\n{date} - {date_h}', size=10, weight='bold')

    # Añadir líneas de la grilla
    bar = ax.gridlines(draw_labels=True, linewidth=1, color='black', alpha=0.8)
    bar.xlocator = mticker.FixedLocator(lons)
    bar.ylocator = mticker.FixedLocator(lats)

    # Mostrar etiquetas solo en el borde superior y izquierdo
    bar.right_labels = False
    bar.top_labels = False

    plt.show()
import xarray
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

era5 = xarray.open_zarr(
    "gs://gcp-public-data-arco-era5/ar/1959-2022-full_37-1h-0p25deg-chunk-1.zarr-v2",
    chunks={'time': 48},
    consolidated=True,
)

#val = era5['temperature'].sel(time=(slice("2021-12-31T21:00:00","2021-12-31T23:00:00"))).time
#print(np.datetime_as_string(val).tolist())

print("mostrando gráfico")
fg = era5['2m_temperature'].sel(time='2021-12-31T21:00:00').plot(robust=True,cmap=mpl.cm.RdYlBu_r)
fg.map_dataarray(xarray.plot.contour, x="longitude", y="latitude", colors="k",levels=13, add_colorbar=False)
plt.show()
print('generado')
plt.savefig("Tomate.jpg")
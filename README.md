# visualize-MZML-file
analysis of MZML file and 2d&amp;3d&amp;heatmap visualization of Msses&amp;Intensiyies&amp;RetentionTime
Reading a MZML file, extract Masses, Intensities, and Retention Time for each spectrum
Notes:
Data1 -> is an excel sheet whish has three columns and we duplicate RT to make every spec has a static specific number of the three variables (mz, intensity, rt)
Data2 -> is an excel sheet whish has two columns and we find the most frequent masse and extract intensity and rt depend on it 
3d -> is a bar 3d plot we put a range of 10 to visualize it cause when the range was so big the plot was not clear
2d -> is a plot for the second dataframe (Data2 excel sheet)
2d-heatmap -> extract the hieghly value of mass and visualize rt and intensity which depend on it 

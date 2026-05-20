"""
Description: Demonstration of the plotting capabilities possible with Font Awesome icons for matplotlib figures.
"""

# Import libraries
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.text as mtext
import matplotlib.transforms as mtransforms
import matplotlib.path as mpath
import numpy as np
import matplotlib.gridspec as mgridspec
import PIL
import matplotlib.patches as mpatches

# Constants
# Dictionary of Font Awesome icons to draw
fa_dict = {
    "google": "\uf1a0",
	"apple": "\uf179",
	"meta": "\ue49b",
	"amazon": "\uf270",
	"microsoft": "\uf17a", 
    "fire": '\uf7e4',
    "moon": '\uf186', 
    "star": '\uf005', 
    "heart": '\uf004', 
    "walk": '\uf554',
    "bicycle": '\uf206', 
    "car": '\uf5e4',
    "bus": '\ue81d',
    "flag": '\uf2b4'
}
    
# Local functions
def CreateAlignedIcon(icon_unicode, icon_font_prop, h_align, v_align, path_size):
    """Function to generate a path from the icon unicode with specified horizontal and vertical alignments. Requires matplotlib.path (as mpath), matplotlib.text (as mtext) and numpy (as np) to be imported.
    AUTHOR:     Mai Tanaka (www.DataDrivenMai.com)
    DATE:       2026-05-11
    REQUIRES:   icon_unicode = unicode for the icon (eg. '\uf005' for the star icon in Font Awesome)
                icon_font_prop = matplotlib.font_manager.FontProperties object for the icon 
                h_align = horizontal alignment (0 = left, 0.5 = center, 1 = right)
                v_align = vertical alignment (0 = bottom, 0.5 = center, 1 = top)
                path_size = path size when generating
    RETURNS:    final_path = a matplotlib.path.Path object with the specified alignments
    """
    
	# Create the initial TextPath to check its max and min values
    test_path = mtext.TextPath((0, 0), icon_unicode, prop=icon_font_prop, size=path_size)

	# Extract the vertices and codes from the test_path
    test_vertices = test_path.vertices
    test_codes = test_path.codes

	# Calculate the max and min coordinates of the icon path
    max_x, max_y = test_path.vertices.max(axis=0)
    min_x, min_y = test_path.vertices.min(axis=0)

	# Calculate the correctional offset required to obtain the desired alignment
    diff_x = max_x - min_x
    diff_y = max_y - min_y
    offset_x = diff_x * h_align
    offset_y = diff_y * v_align
    
	# Resize to make the largest side of the icon=path_size
    if (diff_x > diff_y):
        resize_fac = path_size / diff_x
    else:
        resize_fac = path_size / diff_y

	# Calculate the new vertices by applying the offsets and resizing
    new_vertices = np.zeros_like(test_vertices)
    new_vertices[:, 0] = (test_vertices[:, 0] - min_x - offset_x) * resize_fac 
    new_vertices[:, 1] = (test_vertices[:, 1] - min_y - offset_y) *  resize_fac

	# Create the final path with the new vertices and original code
    final_path = mpath.Path(new_vertices, test_codes)

	# Return the final path
    return final_path

# Main script
def main():
    """Main script that generates plots with subplots that demonstrate how Font Awesome icons can be drawn on matplotlib figures."""

    # Path to your downloaded Font Awesome OTF file
    font_path_brands = "./data/Font Awesome 7 Brands-Regular-400.otf"
    font_path_regular = "./data/Font Awesome 7 Free-Regular-400.otf"
    font_path_solid = "./data/Font Awesome 7 Free-Solid-900.otf"

    # Create FontProperties objects for each of the Font Awesome OTF files
    fp_brands = fm.FontProperties(fname=font_path_brands)
    fp_regular = fm.FontProperties(fname=font_path_regular)
    fp_solid = fm.FontProperties(fname=font_path_solid)

    # Figure 1 (6 subplots): Icon as Text Objects
    fig1, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(13, 8), gridspec_kw={'height_ratios': [1, 3, 4]})
    
    # Fig1, subplot1: Make a figure with minimal parameters for icon placement
    # Place the Google icon at the center of the plot using the brands font
    ax1.text(0.5, 0.5, fa_dict["google"], fontproperties=fp_brands)

    # Plot logistics
    ax1.set_title("Minimal Icon Plotting")
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])

    # Fig 1, subplot2: # Icon rotation angles as a text object
    icon_rotation = [-180, -135, -90, -45, 0, 45, 90, 135, 180]

    # Other parameters of the icon
    icon_size = 20
    icon_color = '#22668D'

    # Make a figure to demonstrate the different font sizes
    # Plot the relative and absolute font sizes
    for i in range(len(icon_rotation)):
        ax2.text(i, 1, fa_dict["meta"], fontproperties=fp_brands, fontsize=icon_size, color=icon_color, rotation=icon_rotation[i])
        
    # Description
    ax2.text(0, 0.7, f"icon rotations from {icon_rotation[0]}° to {icon_rotation[-1]}°", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))

    # Plot logistics
    ax2.set_xlim(-0.5, len(icon_rotation))
    ax2.set_ylim(0.5, 1.5)
    ax2.set_title("Font Rotation Demonstration")
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])    

    # Fig1, subplot3: Three types of color specifications
    font_colors1 = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    font_colors2 = ['#0F172A', '#0A3981', '#22668D', '#8ECDDD', '#D4EBF8', '#FFFADD', '#FFCC70']
    font_colors3 = plt.colormaps['viridis_r']
    icon_size = 20

    # Make a figure to demonstrate the different icon colors
    # Plot the relative and absolute font sizes
    for i in range(len(font_colors1)):
        ax3.text(i, 1, fa_dict["microsoft"], fontproperties=fp_brands, fontsize=icon_size, color=font_colors1[i])
        ax3.text(i, 2, fa_dict["microsoft"], fontproperties=fp_brands, fontsize=icon_size, color=font_colors2[i])
        ax3.text(i, 3, fa_dict["microsoft"], fontproperties=fp_brands, fontsize=icon_size, color=font_colors3(i/len(font_colors1)))

    # Description
    ax3.text(0, 1.45, "color designated with named colors", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    ax3.text(0, 2.45, "color designated with hex codes", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    ax3.text(0, 3.45, "color designated with colormap", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))

    # Plot logistics
    ax3.set_xlim(-0.5, len(font_colors1)-0.25)
    ax3.set_ylim(0.8, 3.7)
    ax3.set_title("Font Color Demonstration")
    ax3.set_xticklabels([])
    ax3.set_yticklabels([])
    
    # Fig 1, subplot4: Relative icon sizes as text objects
    font_sizes1 = ['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
    font_sizes2 = [10, 20, 30, 40, 50, 60, 70]

    # Plot the relative and absolute font sizes
    for i in range(len(font_sizes1)):
        ax4.text(i, 1, fa_dict["apple"], fontproperties=fp_brands, fontsize=font_sizes1[i])
        ax4.text(i, 2, fa_dict["apple"], fontproperties=fp_brands, fontsize=font_sizes2[i])

    # Description
    ax4.text(0, 0.7, "font sizes xx-small to xx-large", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    ax4.text(0, 1.7, "font sizes 10 to 70 points", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))

    # Plot logistics
    ax4.set_xlim(-0.25, len(font_sizes1))
    ax4.set_ylim(0.5, 3.0)
    ax4.set_xticklabels([])
    ax4.set_yticklabels([])
    ax4.set_title("Font Size Demonstration")
    
    # Fig1, subplot5: Combining color, size and location of text objects
    # Designate the icons to plot
    icons = ["google", "apple", "meta", "amazon", "microsoft"]

    # Designate the locations for each icon
    xLoc = [0.2, 0.5, 0.5, 0.5, 0.8]
    yLoc = [0.5, 0.1, 0.5, 0.9, 0.5]

    # Specify color, size and rotation for each icon
    icon_colors = ['#4285F4', '#A2AAAD', '#4267B2', '#FF9900', '#F25022']
    font_sizes = [30, 25, 20, 40, 100]
    icon_rotation = [0, 45, 90, -135, 180]

    #| label: fig-gafam
    #| fig-cap: "Google, Apple, Meta, Amazon and Microsoft icons plotted with different colors, sizes and rotations."

    # Plot the figure with all the icons, colors, sizes and rotations
    for i in range(len(icons)):
        ax5.text(xLoc[i], yLoc[i], fa_dict[icons[i]], fontproperties=fp_brands, color=icon_colors[i], fontsize=font_sizes[i], rotation=icon_rotation[i])
        
        # Scatter plot of icon locations
        ax5.scatter(xLoc[i], yLoc[i], color='black', marker='+')

        # Description
        describe_now = f"Icon: {icons[i].capitalize()}\nColor: {icon_colors[i]}\nSize: {font_sizes[i]} pt\nRotation: {icon_rotation[i]}°"
        ax5.text(xLoc[i], yLoc[i] - 0.05, describe_now, ha='center', va='top', fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))

    # Set the details of the plot before showing
    ax5.set_title("Font Awesome Brand Icons with Different Color, Size and Rotation")
    ax5.set_xlim(0, 1)
    ax5.set_ylim(-0.2, 1)
    ax5.set_xticklabels([])
    ax5.set_yticklabels([])

    # Fig1, subplot 6: Horizontal and vertical alignment options of text objects
    # Various vertical and horizontal alignments to test
    icon_va = ['baseline', 'bottom', 'center', 'center_baseline', 'top']
    icon_ha = ['left', 'center', 'right']

    # Other variables
    icon_color = '#8ECDDD'

    #| label: fig-alignment
    #| fig-cap: "Fifteen different combinations of horizontal and vertical alignments."

    # Create figure
    # Plot the icons with different horizontal and vertical alignments
    for i in range(len(icon_va)):
        for j in range(len(icon_ha)):
            ax6.text(i, j, fa_dict["amazon"], fontproperties=fp_brands, fontsize=20, color=icon_color, ha=icon_ha[j], va=icon_va[i])
            ax6.text(i, j - 0.3, f'ha: {icon_ha[j]}\nva: {icon_va[i]}', fontsize=8, ha='center', va='top', bbox=dict(facecolor='#D4EBF8', alpha=0.5))
            ax6.scatter(i, j, color='black', marker='+')

    # Plot logistics
    ax6.set_xlim(-0.4, len(icon_va)-0.7)
    ax6.set_ylim(-0.65, len(icon_ha)-0.7)
    ax6.set_title("Various Alignment Options", fontsize=14)
    ax6.set_xticklabels([])
    ax6.set_xticklabels([])

    # Logistics for figure 1
    fig1.suptitle('Font Awesome Icons as Text Objects', fontsize=18)
    plt.tight_layout()


    # Figure 2 (6 subplots): Icon as Path Objects
    fig2, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(13, 8), gridspec_kw={'height_ratios': [3, 1, 3]})
    
    # Convert the two variants of the star icon to TextPath object
    star_reg_path = mtext.TextPath((0, 0), fa_dict["star"], prop=fp_regular)
    star_solid_path = mtext.TextPath((0, 0), fa_dict["star"], prop=fp_solid)
    
    # Fig2, subplot1: Path objects drawn with different marker size and color
    # Modify marker size and color
    marker_size = [50, 100, 250, 500, 1000, 2000, 5000]
    icon_colors1 = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    icon_colors2 = ['#0F172A', '#0A3981', '#22668D', '#8ECDDD', '#D4EBF8', '#FFFADD', '#FFCC70']
    icon_colors3 = plt.colormaps['viridis_r']

    # Generate the stars with the plt.scatter function
    for i in range(0, len(marker_size)):
        ax1.scatter(i, 1, color=icon_colors1[i], marker=star_reg_path, s=marker_size[i])
        ax1.scatter(i, 2, color=icon_colors2[i], marker=star_solid_path, s=marker_size[i])
        ax1.scatter(i, 3, color=icon_colors3(i/len(marker_size)), marker=star_reg_path, s=marker_size[i])

    # Description
    ax1.text(0.15, 1.4, "color designated with named colors", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    ax1.text(0.15, 2.4, "color designated with hex codes", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    ax1.text(0.15, 3.4, "color designated with colormap", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))

    # Plot logistics
    ax1.set_xlim(0, len(marker_size))
    ax1.set_ylim(0.8, 3.7)
    ax1.set_title("Marker Color and Size Demonstration")
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])

    # Fig2, subplot2: Demonstration of icon edgecolors
    # Modify size and color
    marker_size = 5000
    icon_colors = ['#0F172A', '#0A3981', '#22668D', '#8ECDDD', '#D4EBF8', '#FFFADD', '#FFCC70']
    edge_colors = plt.colormaps['viridis_r']
    edge_width = 5

    # Generate the stars with the plt.scatter function
    for i in range(0, len(icon_colors)):
        ax2.scatter(i, 1, color=icon_colors[i], marker=star_solid_path, s=marker_size, edgecolor=edge_colors(i/len(icon_colors)), linewidth=edge_width)
        ax2.scatter(i, 2, color=icon_colors[i], marker=star_solid_path, s=marker_size, edgecolor='face', linewidth=edge_width)
        ax2.scatter(i, 3, color=icon_colors[i], marker=star_solid_path, s=marker_size, edgecolor='none', linewidth=edge_width)
        
    # Description
    ax2.text(0.15, 1.55, "edge color different from face color", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    ax2.text(0.15, 2.55, "edge color same as face color", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    ax2.text(0.15, 3.55, "no edge color", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))
    
    # Plot logistics
    ax2.set_title(f"Icon Edge Color Demonstration with Linewidth of {edge_width}")
    ax2.set_xlim(0, len(icon_colors))
    ax2.set_ylim(0.8, 3.8)
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])

    # Fig2, subplot3: Path rotation for icon rotation
    # Generate a default path with no rotation
    fire_path_default = mtext.TextPath((0, 0), fa_dict["fire"], prop=fp_solid)

    # Marker rotation angles
    icon_rotation = [-180, -135, -90, -45, 0, 45, 90, 135, 180]

    # Other icon parameters
    icon_size = 2000
    icon_color = '#8ECDDD'
    edge_color = 'black'

    # Make a figure to demonstrate the different font sizes
    # Plot the relative and absolute font sizes
    for i in range(len(icon_rotation)):
        # Generate a path with rotation using mtransforms.Affine2D().rotate_deg()
        rot_transform = mtransforms.Affine2D().rotate_deg(icon_rotation[i])
        fire_path_rot = fire_path_default.transformed(rot_transform)
            
        # Scatter plot of icon and a '+' to mark the spot
        ax3.scatter(i, 1, color=icon_color, marker=fire_path_rot, s=icon_size, edgecolors=edge_color)
        ax3.scatter(i, 1, color='black', marker='+')
        
    # Description
    ax3.text(3.5, 0.7, f"icon rotations from {icon_rotation[0]}° to {icon_rotation[-1]}°", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))

    # Plot logistics
    ax3.set_xlim(-0.5, len(icon_rotation))
    ax3.set_ylim(0.5, 1.4)
    ax3.set_title("Marker Rotation with `mtransforms.Affine2D().rotate_deg()`")
    ax3.set_xticklabels([])
    ax3.set_yticklabels([])

    # Fig2, subplot4: Path rotation on the spot
    # Generate a default path with no rotation
    fire_path_default = mtext.TextPath((0, 0), fa_dict["fire"], prop=fp_solid)

    # Marker rotation angles
    icon_rotation = [-180, -135, -90, -45, 0, 45, 90, 135, 180]

    # Other icon parameters
    icon_size = 2000
    icon_color = '#22668D'
    edge_color = 'black'

    # Make a figure to demonstrate the different font sizes
    # Plot the relative and absolute font sizes
    for i in range(len(icon_rotation)):
        # Calculate the center point
        max_x, max_y = fire_path_default.vertices.max(axis=0)
        min_x, min_y = fire_path_default.vertices.min(axis=0)
        mid_x = (max_x - min_x) / 2
        mid_y = (max_y - min_y) / 2

        # Generate a path with rotation using mtransforms.Affine2D().rotate_deg_around()
        rot_transform_around = mtransforms.Affine2D().rotate_deg_around(mid_x, mid_y, icon_rotation[i])
        fire_path_rot = fire_path_default.transformed(rot_transform_around)
        
        # Scatter plot of icon and a '+' to mark the spot
        ax4.scatter(i, 1, color=icon_color, marker=fire_path_rot, s=icon_size, edgecolors=edge_color)
        ax4.scatter(i, 1, color='black', marker='+')
        
    # Description
    ax4.text(3.5, 0.7, f"icon rotations from {icon_rotation[0]}° to {icon_rotation[-1]}°", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5))

    # Plot logistics
    ax4.set_xlim(-0.5, len(icon_rotation))
    ax4.set_ylim(0.5, 1.5)
    ax4.set_title("Marker Rotation with mtransforms.Affine2D().rotate_deg_around()")
    ax4.set_xticklabels([])
    ax4.set_yticklabels([])

    # Fig2, subplot5: Horizontal and vertical alignment of paths
    # List of horizontal and vertical alignments to test with path size of 1
    path_size = 1
    icon_halign = [[0.0, 0.5, 1.0], 
                [0.0, 0.5, 1.0],
                [0.0, 0.5, 1.0]]
    icon_valign = [[0.0, 0.0, 0.0], 
                [0.5, 0.5, 0.5],
                [1.0, 1.0, 1.0]]

    # Specify size and color for the icons
    marker_size = 3000
    icon_faceCol = '#FFFADD'
    icon_edgeCol = '#FFCC70'
    edge_width = 2

    # Generate the moon with the plt.scatter function
    for i in range(0, len(icon_halign)):
        for j in range(0, len(icon_halign[0])):
            # Generate the icon with the CreateAlignedIcon function and plot it with plt.scatter
            icon_path = CreateAlignedIcon(fa_dict["moon"], fp_solid, icon_halign[i][j], icon_valign[i][j], path_size)

            # Scatter plot of the icon and a '+' to mark the spot
            ax5.scatter(j, i, color=icon_faceCol, marker=icon_path, s=marker_size, edgecolor=icon_edgeCol, linewidth=edge_width)
            ax5.scatter(j, i, color='black', marker='+')
            
            # Description
            ax5.text(j, i-0.45, f"alignment: {icon_halign[i][j]}, {icon_valign[i][j]}", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5), ha='center')

    # Plot logistics
    ax5.set_title("Icon Alignment After CreateAlignedIcon() Function")
    ax5.set_xlim(-0.5, 2.5)
    ax5.set_ylim(-0.6, 2.1)
    ax5.set_xticklabels([])
    ax5.set_yticklabels([])

    # Fig2, subplot6: Precise manipulation of alignments possible
    # List of horizontal and vertical alignments to test
    path_size = 1
    icon_valign =  0.5
    icon_halign = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

    # Specify size and color for the icons
    marker_size = 3000
    icon_faceCol = '#8ECDDD'
    icon_edgeCol = '#0A3981'
    edge_width = 2

    # Generate the stars with the plt.scatter function
    for i in range(0, len(icon_halign)):
        # Generate the icon with the CreateAlignedIcon function and plot it with plt.scatter
        icon_path = CreateAlignedIcon(fa_dict["moon"], fp_solid, icon_halign[i], icon_valign, path_size)

        # Scatter plot of the icon and a '+' to mark the spot
        ax6.scatter(i, 1, color=icon_faceCol, marker=icon_path, s=marker_size, edgecolor=icon_edgeCol, linewidth=edge_width)
        ax6.scatter(i, 1, color='black', marker='+')
        
        # Description
        ax6.text(i, 0.25, f"h_align: \n{icon_halign[i]}", fontsize=10, bbox=dict(facecolor='#D4EBF8', alpha=0.5), ha='center')

    # Plot logistics
    ax6.set_title("Flexibility of the CreateAlignedIcon() Function")
    ax6.set_xlim(-0.5, len(icon_halign) - 0.5)
    ax6.set_ylim(0, 1.5)
    ax6.set_xticklabels([])
    ax6.set_yticklabels([])

    # Figure 2 logistics
    fig2.suptitle('Font Awesome Icons as Path Objects', fontsize=18)
    plt.tight_layout()

    
    # Figure 3 (4 subplots): Plotting Partial Icons
    fig3 = plt.figure(figsize=(13, 8))
    gs = mgridspec.GridSpec(3, 3, figure=fig3)
    ax1 = fig3.add_subplot(gs[0, 0:2])
    ax2 = fig3.add_subplot(gs[1, 0:2])
    ax3 = fig3.add_subplot(gs[2, 0:2])
    ax4 = fig3.add_subplot(gs[:, 2])
    
    # Fig3, subplot1: Plotting 75 % of a heart icon from the left to right
    # Use CreateAlignedIcon to create a path for the heart icon
    path_size = 100
    heart_path2 = CreateAlignedIcon(fa_dict['heart'], fp_solid, 0, 0, path_size)

    # Define a bounding box for clipping with x_min, y_min, x_max, y_max coordinates
    bbox2 = mtransforms.Bbox.from_extents(0, 0, 0.75*path_size, 1*path_size)

    # Clip the path to the Bbox
    # Set inside=True to show the inside of the box, and inside=False to show the outside of the box
    clipped_heart_path2 = heart_path2.clip_to_bbox(bbox2, inside=True)

    # Set the marker size
    marker_size = 22000
    icon_color = '#C1121F'
    edge_color = 'None'

    # Plot four full hearts
    for i in range(0, 4):
        ax1.scatter(i, 1, marker=heart_path2, s=marker_size, color=icon_color, edgecolors=edge_color)
        
    # Plot three-quarters of a full heart_path
    new_marker_size = marker_size * 0.75
    ax1.scatter(4, 1, marker=clipped_heart_path2, s=new_marker_size, color=icon_color, edgecolors=edge_color)

    # Plot logistics
    ax1.set_xlim(-0.1, 5)
    ax1.set_ylim(0.8, 1.5)
    ax1.set_title('Partial Icons Look Smoother with Large Path Size')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])

    # Fig3, subplot2: Plot 75 % of the heart icon with three quadrants
    # Use CreateAlignedIcon to create a path for the heart icon
    path_size = 100
    heart_path = CreateAlignedIcon(fa_dict['heart'], fp_solid, 0, 0, path_size)

    # Define bounding boxes for clipping with x_min, y_min, x_max, y_max coordinates
    bbox_top = mtransforms.Bbox.from_extents(0, 0.5*path_size, 1*path_size, 1*path_size)
    bbox_left = mtransforms.Bbox.from_extents(0, 0, 0.5*path_size, 1*path_size)

    # Clip the path to the Bbox
    clipped_top = heart_path.clip_to_bbox(bbox_top, inside=True)
    clipped_left = heart_path.clip_to_bbox(bbox_left, inside=True)

    # Set the marker size
    marker_size = 22000
    icon_color = '#C1121F'
    edge_color = 'None'

    # Plot four full hearts
    for i in range(0, 4):
        ax2.scatter(i, 1, marker=heart_path2, s=marker_size, color=icon_color, edgecolors=edge_color)
        
    # Plot three-quarters of a full heart_path
    marker_size_top = marker_size * 1.0
    marker_size_left = marker_size * 0.75
    ax2.scatter(4, 1, marker=clipped_top, s=marker_size_top, color=icon_color, edgecolors=edge_color)
    ax2.scatter(4, 1, marker=clipped_left, s=marker_size_left, color=icon_color, edgecolors=edge_color)

    # Plot logistics
    ax2.set_xlim(-0.1, 5)
    ax2.set_ylim(0.8, 1.5)
    ax2.set_title('Plot Multiple Partial Icons For Complex Shapes')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])

    # Fig3, subplot3: Icon bar graph 1 with one icon representing one commuter
    # Arbitrary dataset we will be visualizing
    commute_data = {"walk": 6, "bicycle": 18, "car": 22, "bus": 14}

    # Constants to use
    path_size = 1
    icon_size = [900, 2100, 1800, 1800]
    icon_color =['#0F172A', '#0A3981', '#22668D', '#8ECDDD']

    # Plot full icons
    for index, (commute_key, commute_value) in enumerate(commute_data.items()):
        for i in range(0, commute_value):
            # Find the icon to plot
            commute_icon = CreateAlignedIcon(fa_dict[commute_key], fp_solid, 0, 0.5, path_size)
            ax3.scatter(i, -index, marker=commute_icon, s=icon_size[index], color=icon_color[index], edgecolors=None)

    # Plot logistics
    ax3.set_xlim([0, 23])
    ax3.set_ylim([-3.4, 0.7])
    ax3.set_xlabel('Number of commuters')
    ax3.set_yticks([-3, -2, -1, 0], ['bus', 'car', 'bike', 'walk'])
    ax3.set_title('Icon Bar Graph with One Icon Representing One Commuter')
    
    # Fig3, subplot4: Icon bar graph 2 with one icon representing 10 commuters
    # Constants to use
    commuter_per_icon = 10
    path_size = 100
    icon_size = [12000, 28000, 24000, 24000]
    partial_marker_size = [7000, 18000, 2800, 3600]
    icon_color = plt.colormaps['viridis_r']([0, 0.333, 0.666, 1.0])
    edge_color = 'None'

    # Plot the icons
    for index, (commute_key, commute_value) in enumerate(commute_data.items()):
        # Create icon
        commute_icon = CreateAlignedIcon(fa_dict[commute_key], fp_solid, 0, 0.5, path_size)
        
        # Plot the full icons
        for i in range(0, commute_value-commuter_per_icon, commuter_per_icon):
            # Plot the full icons
            ax4.scatter(i, -index, marker=commute_icon, s=icon_size[index], color=icon_color[index], edgecolors=edge_color)
            
        # Plot the remaining number as a fraction
        quot_commuters, rem_commuters = divmod(commute_value, commuter_per_icon)
        frac_rem = rem_commuters / commuter_per_icon
        
        # Define bounding boxes for clipping with x_min, y_min, x_max, y_max coordinates
        bbox = mtransforms.Bbox.from_extents(0, -0.5*path_size, frac_rem*path_size, 0.5*path_size)
        
        # Clip the path to the Bbox
        clipped_path = commute_icon.clip_to_bbox(bbox, inside=True)
        
        # Plot the partial icon
        ax4.scatter(quot_commuters * commuter_per_icon, -index, marker=clipped_path, s=partial_marker_size[index], color=icon_color[index], edgecolors=edge_color)

    # Plot logistics
    ax4.set_xlim([-0.5, 30])
    ax4.set_ylim([-3.5, 0.6])
    ax4.set_xlabel('Number of commuters')
    ax4.set_yticks([-3, -2, -1, 0], ['bus', 'car', 'bike', 'walk'])
    ax4.set_title('One Icon Representing Ten Commuters')

    # Figure 3 plot logistics
    fig3.suptitle('Plotting Partial Icons', fontsize=18)
    plt.tight_layout()


    # Figure 4 (2 subplots): Image overlay on icons
    fig4, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    
    # Fig4, subplot1: Image overlay with paths
    # The three flag image file names
    flag_filename = ['./data/canada-flag.jpg', './data/usa-flag.jpg', './data/mexico-flag.png']

    # Create a flag icon to use as the clipping window
    path_size = 100
    flag_path = CreateAlignedIcon(fa_dict['flag'], fp_solid, 0, 0, path_size)
            
    # Plot the three flags one by one
    for i in range(0, len(flag_filename)):
        # Open the flag image one by one with PIL.Image.open
        with PIL.Image.open(flag_filename[i]) as flag_img:
            
            # We'll set the image to be path_size x path_size in size. Note that this will distort the image
            img_x = path_size
            img_y = path_size
            
            # Place the flag image at the specified coordinates
            start_x = i * path_size
            im_now = ax1.imshow(flag_img, extent=[start_x, start_x + img_x, 0, img_y])
            
            # Calculate the transformation required to move the path (centered around the origin) to where the image is placed
            tx = i * path_size 
            ty = 0
            trans_now = mtransforms.Affine2D().translate(tx, ty) + ax1.transData

            # Set the clipping path on top of the flag image
            im_now.set_clip_path(flag_path, transform=trans_now)
            
            # If you want the outline of the flag, you will need to manually play around with the marker size
            # plt.scatter(i * path_size, 0, marker=flag_path, color='None', s=56000, edgecolors='black')
            
    # Plot logistics
    ax1.set_xlim(0, 300)
    ax1.set_ylim(0, 100)
    ax1.set_title('Clipping Images of Size 100x100\nFlag Outlines Difficult to Draw with Paths')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])

    # Fig4, subplot2: Image overlay with patches
    # The three flag image file names
    flag_filename = ['./data/canada-flag.jpg', './data/usa-flag.jpg', './data/mexico-flag.png']

    # Create a flag icon to use as the clipping window
    path_size = 100
    flag_path = CreateAlignedIcon(fa_dict['flag'], fp_solid, 0, 0, path_size)
            
    # Plot the three flags one by one
    for i in range(0, len(flag_filename)):
        # Open the flag image one by one with PIL.Image.open
        with PIL.Image.open(flag_filename[i]) as flag_img:
            
            # Know the original flag image dimensions to eliminate distortion
            img_width, img_height = flag_img.size
            
            # We'll need a correction factor to keep the image undistorted
            corr_fac = path_size / img_height
            img_x = img_width * corr_fac
            img_y = img_height * corr_fac
            # img_x = path_size # If you don't care for distortion, you can use these
            # img_y = path_size 
            
            # Place the flag image at the specified coordinates
            start_x = i * path_size - (img_x - path_size) / 2 # Centers the image on the flag path along the x axis
            im_now = ax2.imshow(flag_img, extent=[start_x, start_x + img_x, 0, img_y])
            
            # Calculate the transformation required to move the path (centered around the origin) to where the image is placed
            tx = i * path_size 
            ty = 0
            trans_now = mtransforms.Affine2D().translate(tx, ty) + ax2.transData

            # Convert the path to a path before clipping
            flag_patch = mpatches.PathPatch(flag_path, transform=trans_now)   # keep patch transform
            im_now.set_clip_path(flag_patch)
            
            # Draw the flag outline using the flag_patch
            ax2.add_patch(flag_patch)
            flag_patch.set_facecolor('None')
            
    # Plot logistics
    ax2.set_xlim(0, 300)
    ax2.set_ylim(0, 100)
    ax2.set_title('Clipping Centered Images without Distortion\nFlag Outlines Easily Drawn with Patches')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])

    # Figure 4 plot logistics
    fig4.suptitle('Image Overlay on Font Awesome Icons', fontsize=18)
    plt.tight_layout()
    plt.show()
    
   
if __name__ == "__main__":
    main()
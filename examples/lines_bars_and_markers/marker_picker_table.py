"""
=======
Marker Picker Table Demo
=======

"""
import matplotlib.pyplot as plt

# create two axes to place canvas table and
# marker picker table separately
fig = plt.figure(figsize=(8, 6))
plt.suptitle("Display markers in first column"
             " of marker picker table")

ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=2)
plt.title("Which day do you have classes?")
# create a 5*6 canvas table
rowLabels = ["Becky", "Cinny", "Eric", "John", "Samuel", "Thezyrie"]
colLabels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
canvasTable = plt.table(
    cellColours=[['#fffacd' for i in range(len(colLabels))]
                 for j in range(len(rowLabels))],
    cellLoc='center',
    rowLabels=rowLabels,
    rowColours=['#b8cbdd' for i in range(len(rowLabels))],
    rowLoc='center',
    colLabels=colLabels,
    colColours=['#b8cbdd' for i in range(len(colLabels))],
    colLoc='center',
    loc='best')
canvasTable.scale(1, 3)
ax1.axis('off')

ax2 = plt.subplot2grid((1, 3), (0, 2), colspan=2)
# a list of customize markers
marker_style = [dict(color='g', marker='*', markersize=8),
                dict(color='r', marker='X', markersize=8),
                dict(color='cornflowerblue', marker='o', markersize=8),
                dict(markerfacecolor='g', markeredgecolor='black',
                     marker='o', fillstyle='left',
                     markerfacecoloralt='r', markersize=8)]
# create a marker picker table for the canvas table
mpTable = plt.table(
    cellText=[["yes"], ["no"], ["many!"], ["maybe?"]],
    # colLabels must be provided if cellText is provided
    # length(colLabels) = length(cellText[0]) + 1(markers column)
    colLabels=["Markers", "Notes"],
    colColours=['#b8cbdd' for i in range(2)],
    rowLabels=["1", "2", "3", "4"],
    rowColours=['#b8cbdd' for i in range(4)],
    cellLoc='center',
    rowLoc="center",
    loc='center',
    markerOptions=marker_style,
    canvasTable=canvasTable,
    # display the marker options in the first column of
    # marker picker table
    drawMarker=True,
    highlightColor="#fcedab")
mpTable.scale(1, 2)
ax2.axis('off')

fig = plt.figure(figsize=(8, 6))
plt.suptitle("Not display markers in first"
             " column of marker picker table")

ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=2)
plt.title("Which day do you have classes?")
# create a 5*6 canvas table
canvasTable = plt.table(
    cellColours=[['#fffacd' for i in range(len(colLabels))]
                 for j in range(len(rowLabels))],
    cellLoc='center',
    rowLabels=rowLabels,
    rowColours=['#b8cbdd' for i in range(len(rowLabels))],
    rowLoc='center',
    colLabels=colLabels,
    colColours=['#b8cbdd' for i in range(len(colLabels))],
    colLoc='center',
    loc='best')
canvasTable.scale(1, 3)
ax1.axis('off')

ax2 = plt.subplot2grid((1, 3), (0, 2), colspan=2)
# create a marker picker table for the canvas table
mpTable = plt.table(
    cellText=[["yes", "good"],
              ["no", "lazy"],
              ["many!", "diligent"],
              ["maybe?", "ha?"]],
    # length(colLabels) = length(cellText[0])
    colLabels=["Markers", "Notes"],
    colColours=['#b8cbdd' for i in range(2)],
    rowLabels=["1", "2", "3", "4"],
    rowColours=['#b8cbdd' for i in range(4)],
    cellLoc='center',
    rowLoc="center",
    loc='center',
    markerOptions=marker_style,
    canvasTable=canvasTable,
    # not display the marker options in the first column
    # of marker picker table
    drawMarker=False,
    highlightColor="#fcedab")
mpTable.scale(1, 2)
ax2.axis('off')

plt.show()

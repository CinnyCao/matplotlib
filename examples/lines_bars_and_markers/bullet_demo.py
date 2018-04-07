import matplotlib.pyplot as plt

# plot a simple bullet chart
# with plt.bullet()
bg_scales1 = [
    [22, 38, 10],
    [30, 25],
    [45, 10, 15]]
data1 = (65, 40, 38)
target_caps1 = (45, 50, 50)
plt.bullet(bg_scales1, data1, target_caps1)

# ----------

# plot the same bullet chart
# through plt.subplots()
bg_scales2 = [
    [22, 38, 10],
    [30, 25],
    [45, 10, 15]]
data2 = (65, 40, 38)
target_caps2 = (45, 50, 50)
fig, ax = plt.subplots()
ax.bullet(bg_scales2, data2, target_caps2)

# ----------

# adding additional arguments
# for better readability
bg_scales3 = [
    [0.3, 0.7, 0.2],
    [0.4, 0.4, 0.6],
    [0.2, 1.2],
    [0.5, 0.3, 0.7]]
bg_labels3 = ['A', 'B', 'C']
data3 = (1.1, 0.9, 1.1, 1.4)
target_caps3 = (0.7, 1.1, 1.3, 1)
fig, ax = plt.subplots()
ax.bullet(bg_scales3, data3, target_caps3,
          label=bg_labels3,
          color=['red', 'orange', '#2a3b1c'],
          cap_color='blue',
          bullet_color='green')
ax.legend()

# ----------

# graph can also be plotted
# horizontally
bg_scales4 = [
    [3, 7, 2],
    [4, 4, 6],
    [5, 3, 7],
    [2, 6, 3],
    [3, 3, 4]]
bg_labels4 = ['A', 'B', 'C']
data4 = (11, 7, 12, 9, 6)
target_caps4 = (7, 11, 9, 4, 8)
fig, ax = plt.subplots()
ax.bullet(bg_scales4, data4, target_caps4,
          label=bg_labels4,
          horizontal=True)
ax.legend()

plt.show()

import matplotlib.pyplot as plt

# define the accuracy values
epochs = [1, 2, 3, 4, 5]
accuracy = [80, 85, 88, 92, 95]

# plot the graph
plt.plot(epochs, accuracy, 'bo-')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Accuracy over Epochs')
plt.show()
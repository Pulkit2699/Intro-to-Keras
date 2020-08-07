# Intro-to-Keras

Using Tensorflow

Functions:

get_dataset(training=True) — takes an optional boolean argument and returns the data as described below.
print_stats(images, labels) — takes the dataset and labels produced by the previous function and prints several statistics about the data; does not return anything.
view_image(image, label) — takes a single image as an array of pixels and displays an image; does not return anything.
build_model() — takes no arguments and returns an untrained neural network as specified below
train_model(model, images, labels, T) — takes the model produced by the previous function and the images and labels produced by the first function and trains the data for T epochs; does not return anything
evaluate_model(model, images, labels, show_loss=True) — takes the trained model produced by the previous function and the test image/labels, and prints the evaluation statistics as described below (displaying the loss metric value if and only if the optional parameter has not been set to False)
predict_label(model, images, index) — takes the trained model and test images, and prints the top 3 most likely labels for the image at the given index, along with their probabilities

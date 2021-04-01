import os
import tensorflow as tf
import matplotlib.pyplot as plt

column_names = ['first', 'second', 'third', 'optimization']
feature_names = column_names[:-1]
label_name = column_names[-1]
class_names = ['no_opt', 'same_opt']

def pack_features_vector(features, labels):
  """Pack the features into a single array."""
  features = tf.stack(list(features.values()), axis=1)
  return features, labels

def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets, training=True)
  return loss_value, tape.gradient(loss_value, model.trainable_variables)

def loss(model, x, y, training):
    # training=training is needed only if there are layers with different
    # behavior during training versus inference (e.g. Dropout).
    y_ = model(x, training=training)
    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    return loss_object(y_true=y, y_pred=y_)

def init_training_procedure(training_data: str, batch_size: int):
  """
  Invoke Tensorflow model training
  """
  train_dataset_fp = training_data

  batch_size = 5

  train_dataset = tf.data.experimental.make_csv_dataset(
    train_dataset_fp,
    batch_size,
    column_names=column_names,
    label_name=label_name,
    num_epochs=1)

  features, labels = next(iter(train_dataset))

  train_dataset = train_dataset.map(pack_features_vector)

  features, labels = next(iter(train_dataset))

  model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(3,)),  # input shape required
    tf.keras.layers.Dense(10, activation=tf.nn.relu),
    tf.keras.layers.Dense(2)
  ])

  predictions = model(features)

  l = loss(model, features, labels, training=False)
  optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

  loss_value, grads = grad(model, features, labels)

  optimizer.apply_gradients(zip(grads, model.trainable_variables))

  print("Step: {},         Loss: {}".format(optimizer.iterations.numpy(),
                                            loss(model, features, labels, training=True).numpy()))

  train_loss_results = []
  train_accuracy_results = []

  num_epochs = 201

  for epoch in range(num_epochs):
    epoch_loss_avg = tf.keras.metrics.Mean()
    epoch_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

    # Training loop - using batches of 32
    for x, y in train_dataset:
      # Optimize the model
      loss_value, grads = grad(model, x, y)
      optimizer.apply_gradients(zip(grads, model.trainable_variables))

      # Track progress
      epoch_loss_avg.update_state(loss_value)  # Add current batch loss
      # Compare predicted label to actual label
      # training=True is needed only if there are layers with different
      # behavior during training versus inference (e.g. Dropout).
      epoch_accuracy.update_state(y, model(x, training=True))

    # End epoch
    train_loss_results.append(epoch_loss_avg.result())
    train_accuracy_results.append(epoch_accuracy.result())

    if epoch % 50 == 0:
      print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                  epoch_loss_avg.result(),
                                                                  epoch_accuracy.result()))
  return model

def init_test_procedure(model, test_data: str, batch_size):
  """
  Test trained Tensorflow model
  """
  test_fp = test_data

  test_dataset = tf.data.experimental.make_csv_dataset(
      test_fp,
      batch_size,
      column_names=column_names,
      label_name=label_name,
      num_epochs=1,
      shuffle=False)

  test_dataset = test_dataset.map(pack_features_vector)

  test_accuracy = tf.keras.metrics.Accuracy()

  for (x, y) in test_dataset:
    # training=False is needed only if there are layers with different
    # behavior during training versus inference (e.g. Dropout).
    logits = model(x, training=False)
    prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
    test_accuracy(prediction, y)

  print("Test set accuracy: {:.3%}".format(test_accuracy.result()))

  tf.stack([y,prediction],axis=1)

def save_model(model):
  """
  Save the Tensorflow model for future use
  """
  pass

def predict_single(model, subdag: list):
  """
  Predicts the optimization on the given subdag
  """
  pass

def predict_multiple(model, subags: list):
  """
  Predicts the optimization on the given subdags
  """
  predict_dataset = tf.convert_to_tensor([
      [281,281,282,],
      [281,546,284,],
      [283,268,283,],
  ])

  # training=False is needed only if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  predictions = model(predict_dataset, training=False)

  for i, logits in enumerate(predictions):
    class_idx = tf.argmax(logits).numpy()
    p = tf.nn.softmax(logits)[class_idx]
    name = class_names[class_idx]
    print("Example {} prediction: {} ({:4.1f}%)".format(i, name, 100*p))

model = init_training_procedure("training_data.csv", 5)
init_test_procedure(model, "training_data.csv", 5)
predict_multiple(model, None)
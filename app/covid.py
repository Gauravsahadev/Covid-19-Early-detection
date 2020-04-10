import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

MODEL_PATH="./frozen_models/frozen_graph.pb"

def wrap_frozen_graph(graph_def, inputs, outputs, print_graph=False):
    def _imports_graph_def():
        tf.compat.v1.import_graph_def(graph_def, name="")
    wrapped_import = tf.compat.v1.wrap_function(_imports_graph_def, [])
    import_graph = wrapped_import.graph
    return wrapped_import.prune(
        tf.nest.map_structure(import_graph.as_graph_element, inputs),
        tf.nest.map_structure(import_graph.as_graph_element, outputs))

def covid_predict(IMAGE_PATH):
    with tf.io.gfile.GFile(MODEL_PATH, "rb") as f:
    graph_def = tf.compat.v1.GraphDef()
    loaded = graph_def.ParseFromString(f.read())

    # Wrap frozen graph to ConcreteFunctions
    frozen_func = wrap_frozen_graph(graph_def=graph_def,
                                    inputs=["x:0"],
                                    outputs=["Identity:0"],
                                    print_graph=True)

    image = cv2.imread(IMAGE_PATH)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    data = np.array([image]) / 255.0
    data=data.astype('float32')
    # Get predictions for images
    predictions = frozen_func(x=tf.constant(data))
    return np.argmax(predictions[0].numpy()[i]
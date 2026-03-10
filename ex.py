import gradio as gr
import tensorflow as tf
import keras
import cv2
import numpy as np


try:
    model = keras.models.load_model('Text_recognizer_Using_CRNN.h5')
except Exception as e:
    print(f"Error loading model: {e}")


def process_image(img):
    """
    Converts image to shape (32, 128, 1) & normalize
    """
    w, h = img.shape
    new_w = 32
    new_h = int(h * (new_w / w))
    img = cv2.resize(img, (new_h, new_w))
    w, h = img.shape

    img = img.astype('float32')

    # Converts each to (32, 128, 1)
    if w < 32:
        add_zeros = np.full((32-w, h), 255)
        img = np.concatenate((img, add_zeros))
        w, h = img.shape

    if h < 128:
        add_zeros = np.full((w, 128-h), 255)
        img = np.concatenate((img, add_zeros), axis=1)
        w, h = img.shape

    if h > 128 or w > 32:
        dim = (128,32)
        img = cv2.resize(img, dim)

    img = cv2.subtract(255, img)

    img = np.expand_dims(img, axis=2)

    # Normalize
    img = img / 255

    return img

def predict_image_text(input_img):
    """
    Predicts text from the input image.
    """
    try:
        # Convert the input image to grayscale
        img = cv2.cvtColor(input_img, cv2.COLOR_RGB2GRAY)
        img = process_image(img)

        # Make predictions using the model
        prediction = model.predict(np.asarray([img]))

        # Convert predictions to log probabilities (optional for some decoders)
        logits = tf.math.log(prediction + 1e-10)  # Adding a small value to avoid log(0)

        # Decode the predictions using CTC greedy decoder
        input_length = np.ones(prediction.shape[0]) * prediction.shape[1]
        input_length = tf.convert_to_tensor(input_length, dtype=tf.int32)

        decoded, _ = tf.nn.ctc_greedy_decoder(
            logits=tf.transpose(logits, perm=[1, 0, 2]),
            sequence_length=input_length
        )

        # Extract dense tensor from the sparse representation
        dense_decoded = tf.sparse.to_dense(decoded[0], default_value=-1).numpy()

        # Define character list
        char_list = "!\"#&'()*+,-./0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        # Extract the predicted text
        temp_text = ""
        for sequence in dense_decoded:
            for p in sequence:
                if p != -1:  # Ignore padding (-1)
                    temp_text += char_list[p]

        return temp_text

    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Some error occurred. Please try again with a proper image."


demo = gr.Interface(predict_image_text, gr.Image(), "text",title="Image to Text Conversion",description="Upload an image and get the extracted text.")
demo.launch(share=False)
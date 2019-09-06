import tensorflow as tf
import utility


@utility.multi_input_model
@utility.named_model
def cnn_multi_input_v2_basic():

    def get_submodel():
        input_ts = tf.keras.layers.Input(shape=(20, 1))
        temp1 = tf.keras.layers.Convolution1D(8, 3, activation="relu")(input_ts)
        temp1 = tf.keras.layers.MaxPooling1D(2)(temp1)
        temp1 = tf.keras.layers.Convolution1D(16, 3, activation="relu")(temp1)
        temp1 = tf.keras.layers.MaxPooling1D(2)(temp1)
        output_ts = tf.keras.layers.Flatten()(temp1)
        return input_ts, output_ts

    inp_list = []
    opt_list = []
    for _ in range(5):
        inp, opt = get_submodel()
        inp_list.append(inp)
        opt_list.append(opt)

    temp2 = tf.concat(opt_list, axis=1)
    temp2 = tf.keras.layers.Dropout(0.5)(temp2)
    temp2 = tf.keras.layers.Dense(32, activation="relu")(temp2)
    temp2 = tf.keras.layers.Dense(8, activation="relu")(temp2)
    output_final = tf.keras.layers.Dense(1, activation="tanh")(temp2)

    model = tf.keras.Model(inputs=inp_list, outputs=output_final)
    model.compile(optimizer='Adam',
                  loss='mae',
                  metrics=['mae', 'mse'])
    return model


@utility.multi_input_model
@utility.named_model
def cnn_multi_input_v2_deep():

    def get_submodel():
        input_ts = tf.keras.layers.Input(shape=(20, 1))
        temp1 = tf.keras.layers.Convolution1D(8, 3)(input_ts)
        temp1 = tf.keras.layers.BatchNormalization(axis=1)(temp1)
        temp1 = tf.keras.layers.LeakyReLU()(temp1)
        temp1 = tf.keras.layers.Convolution1D(8, 3)(temp1)
        temp1 = tf.keras.layers.BatchNormalization(axis=1)(temp1)
        temp1 = tf.keras.layers.LeakyReLU()(temp1)
        temp1 = tf.keras.layers.Convolution1D(8, 3)(temp1)
        temp1 = tf.keras.layers.BatchNormalization(axis=1)(temp1)
        temp1 = tf.keras.layers.LeakyReLU()(temp1)
        temp1 = tf.keras.layers.Convolution1D(8, 3)(temp1)
        temp1 = tf.keras.layers.BatchNormalization(axis=1)(temp1)
        temp1 = tf.keras.layers.LeakyReLU()(temp1)
        temp1 = tf.keras.layers.Convolution1D(8, 3)(temp1)
        temp1 = tf.keras.layers.BatchNormalization(axis=1)(temp1)
        temp1 = tf.keras.layers.LeakyReLU()(temp1)
        output_ts = tf.keras.layers.Flatten()(temp1)
        return input_ts, output_ts

    inp_list = []
    opt_list = []
    for _ in range(5):
        inp, opt = get_submodel()
        inp_list.append(inp)
        opt_list.append(opt)

    temp2 = tf.concat(opt_list, axis=1)
    temp2 = tf.keras.layers.Dense(32, activation="relu")(temp2)
    temp2 = tf.keras.layers.Dropout(0.5)(temp2)
    temp2 = tf.keras.layers.Dense(8, activation="relu")(temp2)
    output_final = tf.keras.layers.Dense(1, activation="tanh")(temp2)

    model = tf.keras.Model(inputs=inp_list, outputs=output_final)
    model.compile(optimizer='Adam',
                  loss='mae',
                  metrics=['mae', 'mse'])
    return model


@utility.multi_input_model
@utility.named_model
def lstm_multi_input_v2_basic():

    def get_submodel():
        input_ts = tf.keras.layers.Input(shape=(20, 1))
        temp1 = tf.keras.layers.LSTM(5, input_shape=(20, 1))(input_ts)
        output_ts = tf.keras.layers.Flatten()(temp1)
        return input_ts, output_ts

    inp_list = []
    opt_list = []
    for _ in range(5):
        inp, opt = get_submodel()
        inp_list.append(inp)
        opt_list.append(opt)

    temp2 = tf.concat(opt_list, axis=1)
    temp2 = tf.keras.layers.Dense(16, activation="relu")(temp2)
    output_final = tf.keras.layers.Dense(1, activation="tanh")(temp2)

    model = tf.keras.Model(inputs=inp_list, outputs=output_final)
    model.compile(optimizer='Adam',
                  loss='mae',
                  metrics=['mae', 'mse'])
    return model


@utility.multi_input_model
@utility.named_model
def lstm_multi_input_v2_stack4():

    def get_submodel():
        input_ts = tf.keras.layers.Input(shape=(20, 1))
        temp1 = tf.keras.layers.LSTM(5, input_shape=(20, 1), return_sequences=True)(input_ts)
        temp1 = tf.keras.layers.LSTM(5, input_shape=(20, 1), return_sequences=True)(temp1)
        temp1 = tf.keras.layers.LSTM(5, input_shape=(20, 1), return_sequences=True)(temp1)
        temp1 = tf.keras.layers.LSTM(5, input_shape=(20, 1))(temp1)
        output_ts = tf.keras.layers.Flatten()(temp1)
        return input_ts, output_ts

    inp_list = []
    opt_list = []
    for _ in range(5):
        inp, opt = get_submodel()
        inp_list.append(inp)
        opt_list.append(opt)

    temp2 = tf.concat(opt_list, axis=1)
    temp2 = tf.keras.layers.Dense(16, activation="relu")(temp2)
    output_final = tf.keras.layers.Dense(1, activation="tanh")(temp2)

    model = tf.keras.Model(inputs=inp_list, outputs=output_final)
    model.compile(optimizer='Adam',
                  loss='mae',
                  metrics=['mae', 'mse'])
    return model


test_iteration1 = [cnn_multi_input_v2_basic,
                   cnn_multi_input_v2_deep,
                   lstm_multi_input_v2_basic,
                   lstm_multi_input_v2_stack4]

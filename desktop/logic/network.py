# Часть 1. Приведение данных в нужный формат для чтения
import pprint
import keras as k
import keras.models
import numpy as np
import tensorflow as tf
import pickle
import os
import random
import matplotlib.pyplot as plt
from keras import models, layers
from keras.optimizers import SGD

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = ''

dic1 = {
    'tcp': '1',
    'udp': '2',
    'icmp': '3'
}
dic2 = {'aol': '1', 'auth': '2', 'bgp': '3', 'courier': '4', 'csnet_ns': '5', 'ctf': '6', 'daytime': '7',
        'discard': '8', 'domain': '9',
        'domain_u': '10',
        'echo': '11', 'eco_i': '12', 'ecr_i': '13', 'efs': '14', 'exec': '15', 'finger': '16', 'ftp': '17',
        'ftp_data': '18',
        'gopher': '19', 'harvest': '20',
        'hostnames': '21', 'http': '22', 'http_2784': '23', 'http_443': '24', 'http_8001': '25', 'imap4': '26',
        'IRC': '27',
        'iso_tsap': '28', 'klogin': '29',
        'kshell': '30', 'ldap': '31', 'link': '32', 'login': '33', 'mtp': '34', 'name': '35', 'netbios_dgm': '36',
        'netbios_ns': '37',
        'netbios_ssn': '38',
        'netstat': '39', 'nnsp': '40', 'nntp': '41', 'ntp_u': '42', 'other': '43', 'pm_dump': '44', 'pop_2': '45',
        'pop_3': '46',
        'printer': '47', 'private': '48',
        'red_i': '49', 'remote_job': '50', 'rje': '51', 'shell': '52', 'smtp': '53', 'sql_net': '54', 'ssh': '55',
        'sunrpc': '56',
        'supdup': '57', 'systat': '58',
        'telnet': '59', 'tftp_u': '60', 'tim_i': '70', 'time': '61', 'urh_i': '62', 'urp_i': '63', 'uucp': '64',
        'uucp_path': '65',
        'vmnet': '66', 'whois': '67',
        'X11': '68', 'Z39_50': '69'}
dic3 = {'OTH': '1', 'REJ': '2', 'RSTO': '3', 'RSTOS0': '4', 'RSTR': '5', 'S0': '6', 'S1': '7', 'S2': '8', 'S3': '9',
        'SF': '10', 'SH': '11'}
dic41 = {
    'apache2': '1',
    'xterm': '2',
    'saint': '3', 'guess_passwd': '4', 'loadmodule': '5', 'ps': '6', 'xlock': '7',
    'imap': '8', 'sqlattack': '9', 'smurf': '10',
    'snmpgetattack': '11', 'warezmaster': '12', 'udpstorm': '13', 'back': '14', 'xsnoop': '15', 'mscan': '16',
    'ftp_write': '17',
    'pod': '18', 'phf': '19', 'mailbomb': '20', 'worm': '21', 'sendmail': '22', 'named': '23', 'portsweep': '24',
    'teardrop': '25',
    'neptune': '26', 'buffer_overflow': '27', 'land': '28', 'snmpguess': '29', 'ipsweep': '30', 'httptunnel': '31',
    'multihop': '32',
    'perl': '33', 'rootkit': '34', 'nmap': '35', 'processtable': '36', 'satan': '37', 'normal': '0'}

def network(path, value):
    k = 0
    help_list = []
    with open(path, 'r') as input_file:
        with open('dataset.txt', 'w') as output_file:
            for line in input_file.readlines():
                elements = line.split(',')
                elements[1] = dic1[elements[1]]
                elements[2] = dic2[elements[2]]
                elements[3] = dic3[elements[3]]
                elements[41] = dic41[elements[41]]
                new_line = ' '.join(elements)
                output_file.write(new_line)
                k = k + 1
                # print(elements)
    # print(set(help_list))

    # Часть 2. Нормализация данных, считывание, приведение в формат, подходящий для нейронной сети.

    count = len(elements)
    # print(count)
    # print(k)

    outputs = []
    inputs = []

    outputs1 = []
    inputs1 = []

    help_list = [0] * count
    # print(output)
    dataset = []

    with open('dataset.txt', 'r') as input_file:
        for line in input_file.readlines():
            elements = line.split(' ')
            for i in range(0, len(elements)):
                elements[i] = float(elements[i])
            # print(elements)
            dataset.append(elements)

    dataset_1 = dataset.copy()

    max_list = [0] * count
    for i in range(0, k):
        for j in range(0, count):
            if max_list[j] < dataset[i][j]:
                max_list[j] = dataset[i][j]

    for i in range(0, k):
        for j in range(0, count):
            if j != 41:
                if max_list[j] != 0:
                    dataset[i][j] /= max_list[j]
                    dataset_1[i][j] /= max_list[j]
            else:
                if dataset[i][j] != 0:
                    dataset[i][j] = 1.0
                else:
                    dataset[i][j] = 0.0

    # print(dataset)

    # сборка массивов на вход нейронной сети

    # для обучения на виды
    outputs_help = []
    inputs_help = []

    # для обучения на типы
    outputs_help1 = []
    inputs_help1 = []
    for i in range(0, k):
        for j in range(0, count - 2):
            inputs_help.append(dataset[i][j])
            inputs_help1.append(dataset_1[i][j])
        outputs_help.append(dataset[i][count - 2])
        outputs_help1.append(dataset_1[i][count - 2])
        outputs.append(outputs_help)
        outputs_help = []
        inputs.append(inputs_help)
        inputs_help = []

        outputs1.append(outputs_help1)
        outputs_help1 = []
        inputs1.append(inputs_help1)
        inputs_help1 = []
    # pprint.pprint(outputs)
    # print(outputs)
    # print(inputs)

    for i in inputs:
        if len(i) != 41:
            print(len(i))

    input_data = np.asarray(inputs, dtype=np.float32)
    output_data = np.asarray(outputs, dtype=np.float32)

    input_data1 = np.asarray(inputs1, dtype=np.float32)
    output_data1 = np.asarray(outputs1, dtype=np.float32)
    # print (input_data)

    '''
    #модель для анализа: опасно или нет
    model1 = models.Sequential()
    model1.add(layers.Dense(units=41, activation="sigmoid"))
    model1.add(layers.Dense(units=20, activation="sigmoid"))
    model1.add(layers.Dense(units=5, activation="sigmoid"))
    model1.add(layers.Dense(units=1, activation="sigmoid"))
    model1.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=["accuracy"])
    fit_results = model1.fit(input_data, output_data, epochs=1000, validation_split=0.1, batch_size=100)
    model1.save("weightsnew.h5")

    #подгрузка сети из файла
    model_loaded = keras.models.load_model("weightsnew.h5")
    #model_loaded.evaluate(inputs, outputs)
    inp = []
    inp.append(input_data[2])
    inp1=np.asarray(inp, dtype=np.float32)
    prediction = model_loaded.predict(inp1)
    #print(prediction)

    prediction1 = model_loaded.predict(inputs)
    #print(prediction1)
    #print(outputs)
    #print(prediction[1])


    plt.title("Losses")
    plt.plot(fit_results.history["loss"], label='Train losses')
    plt.plot(fit_results.history["val_loss"], label='Validation losses')
    plt.legend()
    plt.show()

    plt.title("Accuracy")
    plt.plot(fit_results.history["accuracy"], label='Train accuracy')
    plt.plot(fit_results.history["val_accuracy"], label='Validation accuracy')
    plt.legend()
    plt.show()
    '''

    model = models.Sequential()
    model.add(layers.Dense(41, activation='sigmoid'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(40, activation='sigmoid'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(38, activation='softmax'))
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='sparse_categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.fit(input_data1, output_data1, epochs=1000, batch_size=128)
    model.save("weightsclass.h5")

    # score = model.evaluate(x_test, y_test, batch_size=128)
